/**
 * @author Panait Claudia-Alexandra
 */
import java.sql.*;
import java.time.*;
import java.util.*;

public class BookingManager {
    private List<Booking> bookings;
    private int userId;
    private static Map<Integer, BookingManager> instances = new HashMap<>();
    private Set<String> bookingKeys;

    private BookingManager(int userId) {
        this.userId = userId;
        this.bookings = new ArrayList<>();
        this.bookingKeys = new HashSet<>();
        loadBookings();
    }

    public static BookingManager getInstance(int userId) {
        if (!instances.containsKey(userId)) {
            instances.put(userId, new BookingManager(userId));
        }
        return instances.get(userId);
    }

    private void loadBookings() {
        String sql = "SELECT r.status, r.cod_confirmare, " +
                "cb.id as cat_id, cb.tip_bilet, cb.pret, " +
                "e.id_eveniment, e.denumire, e.descriere, e.tip as event_tip, " +
                "l.denumire as nume_locatie, l.strada, o.denumire as nume_oras, " +
                "d.zi, d.luna, d.an, d.ora, p.cnp " +
                "FROM rezervare r " +
                "JOIN categorie_bilete cb ON r.id_categorie_bilet = cb.id " +
                "JOIN eveniment e ON cb.id_eveniment = e.id_eveniment " +
                "JOIN locatie l ON e.id_locatie = l.id_locatie " +
                "JOIN oras o ON l.id_oras = o.id_oras " +
                "JOIN data_calendaristica d ON e.id_data = d.id_data " +
                "JOIN profil p ON r.id_profil = p.id_profil " +
                "WHERE p.id_utilizator = ?";

        try (Connection conn = DatabaseConnectionSupabase.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setInt(1, this.userId);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                String location = rs.getString("nume_locatie") + " (Str. " + rs.getString("strada") + ")";
                String date = rs.getInt("zi") + "/" + rs.getInt("luna") + "/" + rs.getInt("an") + " la ora " + rs.getTime("ora");
                Event ev = new Event(
                        rs.getInt("id_eveniment"),
                        rs.getString("denumire"),
                        rs.getString("descriere"),
                        rs.getString("event_tip"),
                        location,
                        date,
                        rs.getString("nume_oras")
                );

                TicketCategories category = new TicketCategories(
                        rs.getInt("cat_id"),
                        rs.getString("tip_bilet"),
                        rs.getDouble("pret")
                );

                String statusRezervare = rs.getString("status");
                String codConfirmare = rs.getString("cod_confirmare");

                String national_id = rs.getString("cnp");
                Profile profile = findProfile(national_id);

                if (profile == null && !ProfileManager.getInstance(userId).getProfileList().isEmpty())
                    profile = ProfileManager.getInstance(userId).getProfileList().get(0);


                LocalDate booking_date = LocalDate.of(rs.getInt("an"), rs.getInt("luna"), rs.getInt("zi"));
                LocalTime booking_time = rs.getTime("ora").toLocalTime();

                Booking b = new Booking(profile, ev, booking_date, booking_time, category, statusRezervare, codConfirmare);
                bookings.add(b);

                if (national_id != null)
                    bookingKeys.add(national_id + "_" + ev.getId());

            }
        } catch (SQLException e) {
            System.err.println("Error loading bookings: " + e.getMessage());        }
    }

    public boolean addBooking(Booking b) throws SQLException{
        if (isDuplicate(b))
            throw new SQLException("DUPLICATE_BOOKING");

        String sql_ticket = "INSERT INTO bilet (serie, numar) VALUES (?, ?) RETURNING id_bilet";
        String sql_booking = "INSERT INTO rezervare (id_profil, id_bilet, id_categorie_bilet, status, cod_confirmare) VALUES (?, ?, ?, 'CONFIRMATA', ?)";

        Connection conn = null;
        try {
            conn = DatabaseConnectionSupabase.getConnection();
            conn.setAutoCommit(false); // Începe tranzacția securizată

            int ticket_id = -1;
            // Metoda JDBC standard pentru a lua ID-ul generat automat
            try (PreparedStatement pstmtB = conn.prepareStatement(sql_ticket, Statement.RETURN_GENERATED_KEYS)) {
                pstmtB.setString(1, "SR-" + System.currentTimeMillis());
                pstmtB.setInt(2, new Random().nextInt(10000));
                pstmtB.executeUpdate();

                try (ResultSet generatedKeys = pstmtB.getGeneratedKeys()) {
                    if (generatedKeys.next()) {
                        ticket_id = generatedKeys.getInt(1);
                    }
                }
            }

            if (ticket_id == -1) {
                throw new SQLException("Failed to retrieve auto-generated bilet ID.");
            }

            String code = "CONF-" + UUID.randomUUID().toString().substring(0, 8).toUpperCase();
            try (PreparedStatement pstmtR = conn.prepareStatement(sql_booking)) {
                int idProfil = getIdProfile(b.getProfile().getPerson().getNationalId());

                pstmtR.setInt(1, idProfil);
                pstmtR.setInt(2, ticket_id);
                pstmtR.setInt(3, b.getCategory().getTicketId());
                pstmtR.setString(4, code);
                pstmtR.executeUpdate();
            }

            conn.commit(); // Salvăm definitiv în baza de date

            b.setConfirmation(code);
            bookings.add(b);

            // Salvăm amprenta în setul de cache din memorie
            String national_id = b.getProfile().getPerson().getNationalId();
            bookingKeys.add(national_id + "_" + b.getEvent().getId());

            return true;
        } catch (SQLException e) {
            if (conn != null) {
                try { conn.rollback(); } catch (SQLException ex) { ex.printStackTrace(); }
            }
            // Retrimitem eroarea către Python ca să poată afișa popup-ul de eroare de sistem dacă e cazul
            throw e;
        } finally {
            if (conn != null) {
                try { conn.close(); } catch (SQLException e) { e.printStackTrace(); }
            }
        }
    }

//    public boolean stergeProgramare(Booking p) {
//        String sql = "DELETE FROM rezervare WHERE id_categorie_bilet = ? AND id_profil = ?";
//        try (Connection conn = DatabaseConnectionRender.getConnection();
//             PreparedStatement pstmt = conn.prepareStatement(sql)) {
//
//            int idProfil = getIdProfile(p.getProfile().getPerson().getNationalId());
//
//            pstmt.setInt(1, p.getCategory().getTicketId()); // ID-ul categoriei biletului
//            pstmt.setInt(2, idProfil);                       // ID-ul profilului din DB
//
//            if (pstmt.executeUpdate() > 0) {
//                bookings.remove(p);
//                return true;
//            }
//        } catch (SQLException e) {
//            e.printStackTrace();
//        }
//        return false;
//    }

    private int getIdProfile(String national_id) throws SQLException {
        String sql = "SELECT id_profil FROM profil WHERE cnp = ? AND id_utilizator = ?";
        try (Connection conn = DatabaseConnectionSupabase.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, national_id);
            pstmt.setInt(2, this.userId);
            ResultSet rs = pstmt.executeQuery();
            if (rs.next())
                return rs.getInt("id_profil");
        }
        throw new SQLException("Could not find profile.");
    }

    private boolean isDuplicate(Booking b) {
        if (b == null || b.getProfile() == null || b.getEvent() == null)
            return false;

        String key = b.getProfile().getPerson().getNationalId() + "_" + b.getEvent().getId();
        return bookingKeys.contains(key);
    }

    private Profile findProfile(String national_id) {
        return ProfileManager.getInstance(this.userId).getProfileList().stream()
                .filter(c -> c.getPerson().getNationalId().equals(national_id))
                .findFirst().orElse(null);
    }

    public List<Booking> getBookings() { return bookings; }

    public void refreshBookings() {
        this.bookings.clear();
        this.bookingKeys.clear();
        loadBookings();
    }
}
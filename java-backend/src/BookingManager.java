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

    private BookingManager(int userId) {
        this.userId = userId;
        this.bookings = new ArrayList<>();
        incarcaDinBazaDeDate();
    }

    public static BookingManager getInstance(int userId) {
        if (!instances.containsKey(userId)) {
            instances.put(userId, new BookingManager(userId));
        }
        return instances.get(userId);
    }

    private void incarcaDinBazaDeDate() {
        String sql = "SELECT r.status, r.cod_confirmare, " +
                "cb.id as cat_id, cb.tip_bilet, cb.pret, " +
                "e.id_eveniment, e.denumire, e.descriere, e.tip as event_tip, " +
                "l.denumire as nume_locatie, l.strada, o.denumire as nume_oras, " + // <- o.denumire adăugat aici
                "d.zi, d.luna, d.an, d.ora, p.cnp " +
                "FROM rezervare r " +
                "JOIN categorie_bilete cb ON r.id_categorie_bilet = cb.id " +
                "JOIN eveniment e ON cb.id_eveniment = e.id_eveniment " +
                "JOIN locatie l ON e.id_locatie = l.id_locatie " +
                "JOIN oras o ON l.id_oras = o.id_oras " + // <- JOIN-ul adăugat!
                "JOIN data_calendaristica d ON e.id_data = d.id_data " +
                "JOIN profil p ON r.id_profil = p.id_profil " +
                "WHERE p.id_utilizator = ?";

        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setInt(1, this.userId);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                String location = rs.getString("nume_locatie") + " (Str. " + rs.getString("strada") + ")";
                String date = rs.getInt("zi") + "/" + rs.getInt("luna") + "/" + rs.getInt("an") + " la ora " + rs.getTime("ora");
                String city = rs.getString("nume_oras");
                Event ev = new Event(
                        rs.getInt("id_eveniment"),
                        rs.getString("denumire"),
                        rs.getString("descriere"),
                        rs.getString("event_tip"),
                        location,
                        date,
                        city
                );

                TicketCategories cb = new TicketCategories(
                        rs.getInt("cat_id"),
                        rs.getString("tip_bilet"),
                        rs.getDouble("pret")
                );

                String national_id = rs.getString("cnp");
                Profile profile = findProfile(national_id);

                if (profile == null && !ProfileManager.getInstance(userId).getProfileList().isEmpty()) {
                    profile = ProfileManager.getInstance(userId).getProfileList().get(0);
                }

                LocalDate booking_date = LocalDate.of(rs.getInt("an"), rs.getInt("luna"), rs.getInt("zi"));
                LocalTime booking_time = rs.getTime("ora").toLocalTime();

                bookings.add(new Booking(profile, ev, booking_date, booking_time, cb));
            }
        } catch (SQLException e) {
            System.err.println("Error loading bookings from DB: " + e.getMessage());        }
    }

    public boolean addBooking(Booking b) {
        if (isDuplicate(b)) {
            throw new RuntimeException("DUPLICATE_BOOKING");
        }
        String sqlBilet = "INSERT INTO bilet (serie, numar) VALUES (?, ?) RETURNING id_bilet";
        String sqlRezervare = "INSERT INTO rezervare (id_profil, id_bilet, id_categorie_bilet, status, cod_confirmare) VALUES (?, ?, ?, 'CONFIRMATA', ?)";

        try (Connection conn = DatabaseConnection.getConnection()) {
            conn.setAutoCommit(false);

            int idBiletGenerat;
            try (PreparedStatement pstmtB = conn.prepareStatement(sqlBilet)) {
                pstmtB.setString(1, "SR-" + System.currentTimeMillis());
                pstmtB.setInt(2, new Random().nextInt(10000));
                ResultSet rs = pstmtB.executeQuery();
                rs.next();
                idBiletGenerat = rs.getInt(1);
            }

            try (PreparedStatement pstmtR = conn.prepareStatement(sqlRezervare)) {
                int idProfil = getIdProfile(b.getProfile().getPerson().getNationalId());

                pstmtR.setInt(1, idProfil);
                pstmtR.setInt(2, idBiletGenerat);
                pstmtR.setInt(3, b.getCategory().getId());
                pstmtR.setString(4, "CONF-" + UUID.randomUUID().toString().substring(0, 8).toUpperCase());

                pstmtR.executeUpdate();
            }

            conn.commit();
            bookings.add(b);
            return true;
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }

//    public boolean stergeProgramare(Booking p) {
//        String sql = "DELETE FROM rezervare WHERE id_categorie_bilet = ? AND id_profil = ?";
//        try (Connection conn = DatabaseConnection.getConnection();
//             PreparedStatement pstmt = conn.prepareStatement(sql)) {
//
//            int idProfil = getIdProfile(p.getProfile().getPerson().getNationalId());
//
//            pstmt.setInt(1, p.getCategory().getId()); // ID-ul categoriei biletului
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
        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, national_id);
            pstmt.setInt(2, this.userId);
            ResultSet rs = pstmt.executeQuery();
            if (rs.next()) return rs.getInt("id_profil");
        }
        throw new SQLException("Could not find profile.");
    }

    private boolean isDuplicate(Booking b) {
        return bookings.stream().anyMatch(existing ->
                existing.getProfile().getPerson().getNationalId().equals(b.getProfile().getPerson().getNationalId()) &&
                        existing.getEvent().getId() == b.getEvent().getId() &&
                        existing.getDate().equals(b.getDate())
        );
    }

    private Profile findProfile(String national_id) {
        return ProfileManager.getInstance(this.userId).getProfileList().stream()
                .filter(c -> c.getPerson().getNationalId().equals(national_id))
                .findFirst().orElse(null);
    }

    public List<Booking> getBookings() { return bookings; }
}
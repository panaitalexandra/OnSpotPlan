import java.sql.*;
import java.util.*;

public class EventManager {
    private Map<String, Event> events;
    private static EventManager instance;

    private EventManager() {
        events = new HashMap<>();
        loadEvents();
    }

    private void loadEvents() {
        String sql = "SELECT e.*, l.denumire as nume_locatie, l.strada, o.denumire as nume_oras, d.zi, d.luna, d.an, d.ora " +
                "FROM eveniment e " +
                "JOIN locatie l ON e.id_locatie = l.id_locatie " +
                "JOIN oras o ON l.id_oras = o.id_oras " +
                "JOIN data_calendaristica d ON e.id_data = d.id_data";

        try (Connection conn = DatabaseConnectionSupabase.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                String location = rs.getString("nume_locatie") + " (Str. " + rs.getString("strada") + ")";
                java.time.LocalTime eventTime = rs.getTime("ora").toLocalTime();

                String formattedTime = String.format("%02d:%02d", eventTime.getHour(), eventTime.getMinute());
                String dateTime = rs.getInt("zi") + "/" + rs.getInt("luna") + "/" + rs.getInt("an") + " - " + formattedTime;
                String city = rs.getString("nume_oras");
                Event ev = new Event(
                        rs.getInt("id_eveniment"),
                        rs.getString("denumire"),
                        rs.getString("descriere"),
                        rs.getString("tip"),
                        location,
                        dateTime,
                        city
                );

                loadCategories(conn, ev);
                String key = (ev.getName() + "_" + ev.getLocation() + "_" + ev.getDateTime()).toLowerCase();
                events.put(key, ev);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private void loadCategories(Connection conn, Event ev) {
        String sql = "SELECT id, tip_bilet, pret FROM categorie_bilete WHERE id_eveniment = ?";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, ev.getId());
            try (ResultSet rs = pstmt.executeQuery()) {
                while (rs.next()) {
                    ev.addCategory(new TicketCategories(
                            rs.getInt("id"),
                            rs.getString("tip_bilet"),
                            rs.getDouble("pret")
                    ));
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static EventManager getInstance() {
        if (instance == null) instance = new EventManager();
        return instance;
    }

    public List<Event> getAllEvents() {
        return new ArrayList<>(events.values());
    }
}
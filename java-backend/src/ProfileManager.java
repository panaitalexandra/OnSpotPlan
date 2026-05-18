/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.sql.*;
import java.util.*;

public class ProfileManager {
    private ArrayList<Profile> profiles;
    private int userId;
    private static Map<Integer, ProfileManager> instante = new HashMap<>();

    private ProfileManager(int userId) {
        profiles = new ArrayList<>();
        this.userId = userId;
        loadProfiles();
    }

    private void loadProfiles() {
        String sql = "SELECT * FROM profil WHERE id_utilizator = ?";
        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setInt(1, this.userId);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                profiles.add(new Profile(
                        rs.getString("nume"),
                        rs.getString("prenume"),
                        rs.getString("cnp"),
                        rs.getString("telefon"),
                        rs.getString("regiune"),
                        rs.getString("oras")
                ));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public boolean addProfile(Profile c) {
        Person p = c.getPerson();

        if (!isPhoneValid(p.getPhone_number())) {
            throw new RuntimeException("INVALID_PHONE");
        }
        String sql = "INSERT INTO profil (id_utilizator, nume, prenume, cnp, regiune, oras, telefon) VALUES (?, ?, ?, ?, ?, ?, ?)";

        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, this.userId);
            pstmt.setString(2, p.getLast_name());
            pstmt.setString(3, p.getFirst_name());
            pstmt.setString(4, p.getNationalId());
            pstmt.setString(5, p.getRegion());
            pstmt.setString(6, p.getCity());
            pstmt.setString(7, p.getPhone_number());

            pstmt.executeUpdate();
            profiles.add(c);
            return true;
        } catch (SQLException e) {
            e.printStackTrace();
            if ("23505".equals(e.getSQLState())) {
                throw new RuntimeException("CNP_DUPLICATE");
            }
            return false;
        }
    }
    public boolean deleteProfile(int index) {
        if (index >= 0 && index < profiles.size()) {
            Profile c = profiles.get(index);
            String sql = "DELETE FROM profil WHERE id_utilizator = ? AND cnp = ?";

            try (Connection conn = DatabaseConnection.getConnection();
                 PreparedStatement pstmt = conn.prepareStatement(sql)) {

                pstmt.setInt(1, this.userId);
                pstmt.setString(2, c.getPerson().getNationalId());
                pstmt.executeUpdate();

                profiles.remove(index);
                return true;
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        return false;
    }
    public boolean updateProfile(int index, Profile profileNou) {
        if (index >= 0 && index < profiles.size()) {
            Person p = profileNou.getPerson();

            if (!isPhoneValid(p.getPhone_number())) {
                throw new RuntimeException("INVALID_PHONE");
            }

            Profile profileVechi = profiles.get(index);

            String sql = "UPDATE profil SET nume=?, prenume=?, cnp=?, regiune=?, oras=?, telefon=? " +
                    "WHERE id_utilizator = ? AND cnp = ?";

            try (Connection conn = DatabaseConnection.getConnection();
                 PreparedStatement pstmt = conn.prepareStatement(sql)) {

                pstmt.setString(1, p.getLast_name());
                pstmt.setString(2, p.getFirst_name());
                pstmt.setString(3, p.getNationalId());
                pstmt.setString(4, p.getRegion());
                pstmt.setString(5, p.getCity());
                pstmt.setString(6, p.getPhone_number());

                pstmt.setInt(7, this.userId);
                pstmt.setString(8, profileVechi.getPerson().getNationalId());

                int rowsAffected = pstmt.executeUpdate();
                if (rowsAffected > 0) {
                    profiles.set(index, profileNou);
                    return true;
                }
            } catch (SQLException e) {
                e.printStackTrace();
                if ("23505".equals(e.getSQLState())) {
                    throw new RuntimeException("CNP_DUPLICATE");
                }
            }
        }
        return false;
    }
    public ArrayList<Profile> getProfileList() {
        return profiles;
    }
    private boolean isPhoneValid(String telefon) {
        if (telefon == null)
            return false;
        String curatat = telefon.replaceAll("[\\s\\-\\(\\)]", "");
        return curatat.matches("^\\+?\\d{7,15}$");
    }
    public static ProfileManager getInstance(int userId) {
        if (!instante.containsKey(userId)) {
            instante.put(userId, new ProfileManager(userId));
        }
        return instante.get(userId);
    }
}
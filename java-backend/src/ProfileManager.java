/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.sql.*;
import java.util.*;

public class ProfileManager {
    private ArrayList<Profile> profiles;
    private int userId;
    private static Map<Integer, ProfileManager> instances = new HashMap<>();

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

    public boolean addProfile(Profile c) throws Exception {
        Person p = c.getPerson();

        if (!isPhoneValid(p.getPhone_number())) {
            throw new RuntimeException("The entered phone number is invalid. It must be between 7 and 15 digits long and can include optional spaces, dashes, or a '+' prefix.");
        }
        if (p.getNationalId() == null || p.getNationalId().trim().isEmpty())
            throw new Exception("The National ID field cannot be empty. Please provide a valid identification document number.");
        String id = p.getNationalId().trim();
        if (!id.matches("^[a-zA-Z0-9]{5,20}$"))
            throw new Exception("The National ID format is invalid. It must be between 5 and 20 characters long and contain only letters and numbers (no special characters or spaces).");

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
                throw new Exception("This National ID is already registered to another profile in our database.");
            }
            throw new Exception("A database error occurred while trying to save the profile: " + e.getMessage());
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
    public boolean updateProfile(int index, Profile profileNou) throws Exception {
        if (index >= 0 && index < profiles.size()) {
            Person p = profileNou.getPerson();

            if (!isPhoneValid(p.getPhone_number())) {
                throw new Exception("The entered phone number is invalid. It must be between 7 and 15 digits long and can include optional spaces, dashes, or a '+' prefix.");
            }
            if (p.getNationalId() == null || p.getNationalId().trim().isEmpty())
                throw new Exception("The National ID field cannot be empty. Please provide a valid identification document number.");
            String id = p.getNationalId().trim();
            if (!id.matches("^[a-zA-Z0-9]{5,20}$"))
                throw new Exception("The National ID format is invalid. It must be between 5 and 20 characters long and contain only letters and numbers (no special characters or spaces).");

            Profile oldProfile = profiles.get(index);

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
                pstmt.setString(8, oldProfile.getPerson().getNationalId());

                int rowsAffected = pstmt.executeUpdate();
                if (rowsAffected > 0) {
                    profiles.set(index, profileNou);
                    return true;
                }
            } catch (SQLException e) {
                e.printStackTrace();
                if ("23505".equals(e.getSQLState()))
                    throw new Exception("This National ID is already registered to another profile in our database.");
                throw new Exception("A database error occurred while trying to update the profile: " + e.getMessage());
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
        if (!instances.containsKey(userId)) {
            instances.put(userId, new ProfileManager(userId));
        }
        return instances.get(userId);
    }
}
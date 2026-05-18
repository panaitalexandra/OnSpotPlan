/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.sql.*;
import java.util.*;

public class UserManager {
    private ArrayList<User> users;
    private static UserManager instanta;

    private UserManager() {
        users = new ArrayList<>();
        loadUsers();
    }

    private void loadUsers() {
        String sql = "SELECT id_utilizator, email, parola FROM utilizatori";
        try (Connection conn = DatabaseConnection.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                User user = new User(
                        rs.getString("email"),
                        rs.getString("parola")
                );
                user.setId(rs.getInt("id_utilizator"));
                users.add(user);
            }
        } catch (Exception e) {
            System.err.println("Loading error: " + e.getMessage());
        }
    }
    public int getIdByEmail(String email) {
        for (User u : users) {
            if (u.getEmail().equalsIgnoreCase(email)) return u.getId();
        }
        return -1;
    }
    public void saveUser(User userNou) {
        String sql = "INSERT INTO utilizatori (email, parola) VALUES (?, ?) " +
                "ON CONFLICT (email) DO UPDATE SET parola = EXCLUDED.parola";

        try (Connection conn = DatabaseConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {

            pstmt.setString(1, userNou.getEmail());
            pstmt.setString(2, userNou.getParola());

            pstmt.executeUpdate();

            try (ResultSet generatedKeys = pstmt.getGeneratedKeys()) {
                if (generatedKeys.next()) {
                    int idGenerat = generatedKeys.getInt(1);
                    userNou.setId(idGenerat);
                }
            }

        } catch (SQLException e) {
            System.err.println("Could not save userr: " + e.getMessage());
            e.printStackTrace();
        }
    }


    public boolean isEmailValid(String email) {
        return EmailValidation.isValid(email);
    }

    public boolean isEmailRegistered(String email) {
        for (User user : users)
            if (user.getEmail().equalsIgnoreCase(email.trim()))
                return true;
        return false;
    }
    public boolean isPasswordValid(String parola) {
        return PasswordValidation.hasMinLength(parola) &&
                PasswordValidation.containsUppercase(parola) &&
                PasswordValidation.containsNum(parola) &&
                PasswordValidation.containsSpecial(parola);
    }

    public User storeUser(String email, String parola) {
        if (!isEmailValid(email)) return null;
        if (isEmailRegistered(email)) return null;
        if (!isPasswordValid(parola)) return null;

        var user = new User(email, parola);
        saveUser(user);
        users.add(user);
        return user;
    }
    
    public User getUser(String email, String parola){
        for(User user: users)
            if(user.authentificate(email, parola))
                return user;
        return null;
    }

    
    public static UserManager getInstance(){
        if(instanta == null)
            instanta = new UserManager();
        return instanta;
    }
}
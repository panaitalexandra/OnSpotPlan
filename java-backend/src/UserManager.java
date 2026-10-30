/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.sql.*;
import java.util.*;

public class UserManager {
    private Map<String,User> users;
    private static UserManager instance;

    private UserManager() {
        users = new HashMap<>();
        loadUsers();
    }

    private void loadUsers() {
        String sql = "SELECT id_utilizator, email, parola FROM utilizatori";
        try (Connection conn = DatabaseConnectionSupabase.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                User user = new User(
                        rs.getString("email"),
                        rs.getString("parola")
                );
                user.setId(rs.getInt("id_utilizator"));
                users.put(user.getEmail().toLowerCase().trim(), user);
            }
        } catch (Exception e) {
            System.err.println("Loading error: " + e.getMessage());
        }
    }
    public int getIdByEmail(String email) {
        if (email == null)
            return -1;
        User u = users.get(email.toLowerCase().trim());
        return (u != null) ? u.getId() : -1;
    }
    public void saveUser(User userNou) {
        String sql = "INSERT INTO utilizatori (email, parola) VALUES (?, ?) " +
                "ON CONFLICT (email) DO UPDATE SET parola = EXCLUDED.parola";

        try (Connection conn = DatabaseConnectionSupabase.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {

            pstmt.setString(1, userNou.getEmail());
            pstmt.setString(2, userNou.getPassword());

            pstmt.executeUpdate();

            try (ResultSet generatedKeys = pstmt.getGeneratedKeys()) {
                if (generatedKeys.next()) {
                    int idGenerat = generatedKeys.getInt(1);
                    userNou.setId(idGenerat);
                }
            }

        } catch (SQLException e) {
            System.err.println("Could not save user: " + e.getMessage());
            e.printStackTrace();
        }
    }

    public boolean isEmailValid(String email) {
        return EmailValidation.isValid(email);
    }

    public boolean isEmailRegistered(String email) {
        if (email == null) return false;
        return users.containsKey(email.toLowerCase().trim());
    }
    public boolean isPasswordValid(String parola) {
        return PasswordValidation.hasMinLength(parola) &&
                PasswordValidation.containsUppercase(parola) &&
                PasswordValidation.containsNum(parola) &&
                PasswordValidation.containsSpecial(parola);
    }

    public User storeUser(String email, String parola) throws Exception {
        if (!isEmailValid(email))
            throw new Exception("INVALID_EMAIL_FORMAT");

        if (isEmailRegistered(email))
            throw new Exception("EMAIL_ALREADY_EXISTS");

        if (!isPasswordValid(parola))
            throw new Exception("WEAK_PASSWORD");

        User user = new User(email, parola);
        saveUser(user);
        users.put(user.getEmail().toLowerCase().trim(), user);
        return user;
    }

    public User getUser(String email, String password) throws Exception {
        User user = findUserByEmail(email);
        if (user == null)
            throw new Exception("EMAIL_NOT_FOUND");

        if (!user.getPassword().equals(password))
            throw new Exception("INCORRECT_PASSWORD");

        return user;
    }

    public User findUserByEmail(String email) {
        if (email == null) return null;
        return users.get(email.toLowerCase().trim());
    }

    public static UserManager getInstance(){
        if(instance == null)
            instance = new UserManager();
        return instance;
    }
}
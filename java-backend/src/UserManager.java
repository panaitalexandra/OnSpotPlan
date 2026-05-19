/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.sql.*;
import java.util.*;

public class UserManager {
    private ArrayList<User> users;
    private static UserManager instance;

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

    public User storeUser(String email, String parola) throws Exception {
        if (!isEmailValid(email)) {
            throw new Exception("INVALID_EMAIL_FORMAT");
        }
        if (isEmailRegistered(email)) {
            throw new Exception("EMAIL_ALREADY_EXISTS");
        }
        if (!isPasswordValid(parola)) {
            throw new Exception("WEAK_PASSWORD");
        }

        User user = new User(email, parola);
        saveUser(user);
        users.add(user);
        return user;
    }

    public User getUser(String email, String password) throws Exception {

        User user = findUserByEmail(email);
        if (user == null) {
            throw new Exception("EMAIL_NOT_FOUND");
        }

        if (!user.getPassword().equals(password)) {
            throw new Exception("INCORRECT_PASSWORD");
        }

        return user;
    }

    public User findUserByEmail(String email) {
        if (email == null) return null;
        for (User u : users)
            if (u.getEmail().equalsIgnoreCase(email.trim()))
                return u;
        return null;
    }
    public static UserManager getInstance(){
        if(instance == null)
            instance = new UserManager();
        return instance;
    }
}
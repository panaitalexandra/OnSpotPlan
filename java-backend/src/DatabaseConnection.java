import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnection {
    private static final String URL = "jdbc:postgresql://db.jvrgvusbfdvuaymucuud.supabase.co:5432/postgres";
    private static final String USER = "postgres";
    private static final String PASSWORD = "eventhubwelcomeapril";

    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }
}
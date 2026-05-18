import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class TestSupabase {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://db.jvrgvusbfdvuaymucuud.supabase.co:5432/postgres";
        String user = "postgres";
        String password = "eventhubwelcomeapril";

        try (Connection conn = DriverManager.getConnection(url, user, password)) {
            System.out.println("✅ Conectat la Supabase!");

            Statement st = conn.createStatement();
            ResultSet rs = st.executeQuery("SELECT count(*) FROM eveniment"); // Test pe tabelul tau

            if (rs.next()) {
                System.out.println("Număr evenimente în DB: " + rs.getInt(1));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
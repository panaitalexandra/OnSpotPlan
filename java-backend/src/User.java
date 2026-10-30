/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.util.*;

public class User {
    private int id;
    private List<Profile> profiles;
    private Person p;

    public User(String email, String password){
        p = new Person(email, password);
        this.profiles = new ArrayList<>();
    }

    public User(String last_name, String first_name, String national_id, String region, String city, String phone, String email, String password) throws Exception {
        p = new Person(last_name, first_name, national_id, region, city, phone);
        this.profiles = new ArrayList<>();
        p.setEmail(email);
        p.setPassword(password);
    }
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

     public boolean authentificate(String email, String password) {
        return p.getEmail().equals(email) && p.getPassword().equals(password);
    }
    public String getEmail() {
        return p.getEmail();
    }
    public String getPassword() {
        return p.getPassword();
    }
    public Person getPerson() {
        return this.p;
    }

}

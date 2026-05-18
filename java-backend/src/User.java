/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.io.*;
import java.util.*;

public class User {
    private int id;
    private List<Profile> profiles;
    private boolean profile_completed;
    private Person p;

    public User(String email, String password){
        p = new Person(email, password);
        this.profiles = new ArrayList<>();
        this.profile_completed = false;
    }

    public User(String last_name, String first_name, String national_id, String region, String city, String phone, String email, String password) throws Exception {
        p = new Person(last_name, first_name, national_id, region, city, phone);
        this.profiles = new ArrayList<>();
        this.profile_completed = false;

        try{
            if (!PasswordValidation.validation(password))
                throw new Exception("Password does not match requirements");
        }catch(IOException e){ e.printStackTrace(); }
        
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
    public String getParola() {
        return p.getPassword();
    }
    public Person getPerson() {
        return this.p;
    }
//    @Override
//    public String toString() {
//        if (p.getLast_name() == null || p.getLast_name().isEmpty())
//            return String.join("|", p.getEmail(), p.getPassword());
//        else
//        {
//            return String.join("|",
//                p.getLast_name(),
//                p.getFirst_name(),
//                p.getNationalId(),
//                p.getRegion(),
//                p.getCity(),
//                p.getPhone_number(),
//                p.getEmail(),
//                p.getPassword()
//            );
//        }
//    }
}

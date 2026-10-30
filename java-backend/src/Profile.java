/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.time.*;

public class Profile {
    private Person p;

    public Profile(String last_name, String first_name, String id, String phone, String region, String city) {
        this.p = new Person(last_name, first_name, id, region, city, phone);
    }

    public Person getPerson(){
        p.setIdentity_card(p.getIdentity_card());
        return p;
    }

    public String getPhone_number() { return p.getPhone_number(); }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Profile that = (Profile) o;
        return p.getNationalId().equals(that.p.getNationalId());
    }
}
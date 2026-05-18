/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.time.*;

public class Profile {
    private int varsta;
    private Person p;

    public Profile(String last_name, String first_name, String id, String phone){
        p = new Person(last_name, first_name, id, phone);
        this.varsta = checkAge(id);
    }
    public Profile(String last_name, String first_name, String id, String phone, String region, String city) {
        this.p = new Person(last_name, first_name, id, region, city, phone);
        this.varsta = checkAge(id);
    }
    public Person getPerson(){
        p.setIdentity_card(p.getIdentity_card());
        return p;
    }

    int checkAge(String cnp) {
        if(cnp == null || cnp.length() != 13){
            System.out.println("Invalid ID");
            return -1;
        }
        try {
            char sex = cnp.charAt(0);
            int an = Integer.parseInt(cnp.substring(1, 3));
            int luna = Integer.parseInt(cnp.substring(3, 5));
            int zi = Integer.parseInt(cnp.substring(5, 7));

            int anNastere = switch (sex) {
                case '1', '2' -> 1900 + an;
                case '5', '6' -> 2000 + an;
                default -> throw new IllegalArgumentException("Invalid ID");
            };
            LocalDate dataNastere = LocalDate.of(anNastere, luna, zi);
            return Period.between(dataNastere, LocalDate.now()).getYears();
        }catch (IllegalArgumentException e) {
            System.out.println("Eroare" + e.getMessage());
            return -1;
        }
    }

    public int getVarsta() {
        return varsta;
    }

    public String getPhone_number() {
        return p.getPhone_number();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Profile that = (Profile) o;
        return p.getNationalId().equals(that.p.getNationalId());
    }
}
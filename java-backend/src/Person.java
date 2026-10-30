/**
 *
 * @author Panait Claudia-Alexandra
 */
public class Person {
    private String last_name, first_name, email, password, phone_number;
    private IdentityCard identity_card;

    public Person(String last_name, String first_name, String national_id, String region, String city, String phone_number){
        this.last_name = last_name;
        this.first_name = first_name;
        this.identity_card = new IdentityCard(national_id, region, city);
        this.phone_number = phone_number;

    }
    public Person(String email, String password){
        this.email = email;
        this.password = password;
    }
    public IdentityCard getIdentity_card() {
        return identity_card;
    }
    public void setIdentity_card(IdentityCard identity_card) {
        this.identity_card = identity_card;
    }

    public String getNationalId(){
        return identity_card.getNationalId();
    }
    public String getRegion(){
        return identity_card.getRegion();
    }
    public String getCity(){
        return identity_card.getCity();
    }

    public void setEmail(String email){
        this.email = email;
    }
    public void setPassword(String password){
        this.password = password;
    }

    public String getLast_name(){
        return this.last_name;
    }
    public String getFirst_name(){
        return this.first_name;
    }
    public String getEmail(){
        return this.email;
    }
    public String getPassword(){
        return this.password;
    }
    public String getPhone_number(){
        return this.phone_number;
    }
}

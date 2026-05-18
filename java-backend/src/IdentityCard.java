/**
 *
 * @author Panait Claudia-Alexandra
 */
public class IdentityCard {
    private String national_id, region, city;
    public IdentityCard(String national_id, String region, String city){
        this.national_id = national_id;
        this.region = region;
        this.city = city;
    }
    public IdentityCard(String national_id){
        this.national_id = national_id;
    }
    public String getNationalId(){
        return this.national_id;
    }
    public String getRegion(){
        return this.region;
    }
    public String getCity(){
        return this.city;
    }
}

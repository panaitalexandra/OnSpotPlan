/**
 *
 * @author Panait Claudia-Alexandra
 */
public class IdentityCard {
    private String CNP, series, number, region, city;
    public IdentityCard(String cnp, String series, String numar, String region, String city){
        this.CNP = cnp;
        this.series = series;
        this.number = numar;
        this.region = region;
        this.city = city;
    }
    public IdentityCard(String cnp){
        this.CNP = cnp;
    }
    public String getCnp(){
        return this.CNP;
    }
    public String getSeries(){
        return this.series;
    }
    public String getNumber(){
        return this.number;
    }
    public String getRegion(){
        return this.region;
    }
    public String getCity(){
        return this.city;
    }
}

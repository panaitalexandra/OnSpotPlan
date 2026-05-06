/**
 *
 * @author Panait Claudia-Alexandra
 */
public class Persoana {
    private String nume, prenume, email, parola, telefon;
    private IdentityCard buletin;
    
    public Persoana(String nume, String prenume, String cnp, String telefon){// constructor necesar pentru clasa Client
        this.nume = nume;
        this.prenume = prenume;
        this.buletin = new IdentityCard(cnp);
        this.telefon = telefon;
    }
    public Persoana(String nume, String prenume, String cnp, String serie, String numar, String jud, String loc, String telefon){// constructor necesar pentru clasele Client si Utilizator
        this.nume = nume;
        this.prenume = prenume;
        this.buletin = new IdentityCard(cnp, serie, numar, jud, loc);
        this.telefon = telefon;

    }
    public Persoana(String email, String parola){
        this.email = email;
        this.parola = parola;
    }
    public String getNume(){
        return this.nume;
    }
    public String getPrenume(){
        return this.prenume;
    }
    public String getEmail(){
        return this.email;
    }
    public String getParola(){
        return this.parola;
    }
    public String getCNP(){
        return buletin.getCnp();
    }
    public String getSeries(){
        return buletin.getSeries();
    }
    public String getNumar(){
        return buletin.getNumber();
    }
    public String getRegion(){
        return buletin.getRegion();
    }
    public String getLocalitate(){
        return buletin.getCity();
    }
    public void setEmail(String email){
        this.email = email;
    }
    public void setParola(String parola){
        this.parola = parola;
     }
    public IdentityCard getCarteIdentitate() {
        return buletin;
    }
    public void setCarteIdentitate(IdentityCard buletin) {
        this.buletin = buletin;
    }
    public String getTelefon(){
        return this.telefon;
    }

}

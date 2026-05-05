/**
 *
 * @author Panait Claudia-Alexandra
 */
public class Persoana {
    private String nume, prenume, email, parola, telefon;
    private ActIdentitate buletin;
    
    public Persoana(String nume, String prenume, String cnp, String telefon){// constructor necesar pentru clasa Client
        this.nume = nume;
        this.prenume = prenume;
        this.buletin = new ActIdentitate(cnp);
        this.telefon = telefon;
    }
    public Persoana(String nume, String prenume, String cnp, String serie, String numar, String jud, String loc, String telefon){// constructor necesar pentru clasele Client si Utilizator
        this.nume = nume;
        this.prenume = prenume;
        this.buletin = new ActIdentitate(cnp, serie, numar, jud, loc);
        this.telefon = telefon;

    }
    public Persoana(String email, String parola){// constructor necesar pentru clasa Utilizator
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
    public String getSerie(){
        return buletin.getSerie();
    }
    public String getNumar(){
        return buletin.getNumar();
    }
    public String getJudet(){
        return buletin.getJudet();
    }
    public String getLocalitate(){
        return buletin.getLocalitate();
    }
    public void setEmail(String email){
        this.email = email;
    }
    public void setParola(String parola){
        this.parola = parola;
     }
    public ActIdentitate getCarteIdentitate() {
        return buletin;
    }
    public void setCarteIdentitate(ActIdentitate buletin) {
        this.buletin = buletin;
    }
    public String getTelefon(){
        return this.telefon;
    }

}

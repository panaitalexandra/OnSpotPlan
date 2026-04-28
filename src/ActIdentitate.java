/**
 *
 * @author Mihaila ALexia-Andreea
 */
public class ActIdentitate {
    private String CNP, serie, numar, judet, localitate;
    public ActIdentitate(String cnp, String serie, String numar, String judet, String loc){
        this.CNP = cnp;
        this.serie = serie;
        this.numar = numar;
        this.judet = judet;
        this.localitate = loc;
    }
    public ActIdentitate(String cnp){
        this.CNP = cnp;
    }
    public String getCnp(){
        return this.CNP;
    }
    public String getSerie(){
        return this.serie;
    }
    public String getNumar(){
        return this.numar;
    }
    public String getJudet(){
        return this.judet;
    }
    public String getLocalitate(){
        return this.localitate;
    }
}

/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.io.*;
import java.util.*;

public class Utilizator {

    private List<Client> beneficiari;
    private boolean profilComplet;
    private Persoana p;
   
    public Utilizator(String email, String parola){// constructor necesar pentru ManagerUtilizatori
        p = new Persoana(email, parola);
        this.beneficiari = new ArrayList<>();
        this.profilComplet = false;
    }
    
    public Utilizator(String nume, String prenume, String cnp, String serie, String numar, String judet, String localitate, String telefon, String email, String parola) throws Exception {// constructor necesar pentru ManagerUtilizatori
        p = new Persoana(nume, prenume, cnp, serie, numar, judet, localitate, telefon);
        this.beneficiari = new ArrayList<>();
        this.profilComplet = false;

        try{
        if (!ValidatorParola.esteValida(parola)) 
            throw new Exception("Parola nu respecta cerintele de securitate");
        }catch(IOException e){ e.printStackTrace(); }
        
        p.setEmail(email);
        p.setParola(parola);
        
    }
     public boolean autentificare(String email, String parola) {
        return p.getEmail().equals(email) && p.getParola().equals(parola);
    }
    public String getEmail() {
        return p.getEmail();
    }
    public String getParola() {
        return p.getParola();
    }
    @Override
    public String toString() {
        if (p.getNume() == null || p.getNume().isEmpty()) 
            return String.join("|", p.getEmail(), p.getParola());
        else 
        {
            return String.join("|",
                p.getNume(),
                p.getPrenume(),
                p.getCNP(),
                p.getSeries(),
                p.getNumar(),
                p.getRegion(),
                p.getLocalitate(),
                p.getTelefon(),
                p.getEmail(),
                p.getParola()
            );
        }
    }
}

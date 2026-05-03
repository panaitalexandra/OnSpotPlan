/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.time.*;

public class Client {
    private int varsta;
    private Persoana p;
    private String telefon;

    public Client(String nume, String prenume, String cnp, String telefon){
        p = new Persoana(nume, prenume, cnp);
        this.telefon = telefon;
        this.varsta = calculeazaVarsta(cnp);
    }
    public Client(String nume, String prenume, String cnp, String serie, String numar, String judet, String localitate, String telefon) {
        this.p = new Persoana(nume, prenume, cnp, serie, numar, judet, localitate);
        this.telefon = telefon;
        this.varsta = calculeazaVarsta(cnp);
    }
    public Persoana getPersoana(){
        p.setCarteIdentitate(p.getCarteIdentitate());
        return p;
    }

    int calculeazaVarsta(String cnp) {
        if(cnp == null || cnp.length() != 13){
            System.out.println("CNP invalid");
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
                default -> throw new IllegalArgumentException("CNP invalid");
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

    public String getTelefon() {
        return telefon;
    }

    public void setTelefon(String telefon) {
        this.telefon = telefon;
    }

    @Override
    public String toString() {
        return p.getNume() + " " + p.getPrenume() + ", CNP: " + p.getCNP() + ", varsta: " + varsta;// + ", risc: " + dizabilitate;
    }
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Client that = (Client) o;
        return p.getCNP().equals(that.p.getCNP());
    }
}
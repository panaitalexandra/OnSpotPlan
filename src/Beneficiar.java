/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.time.*;

public class Beneficiar {
    private int varsta;
    private Persoana p;
    //private String dizabilitate;

    public Beneficiar(String nume, String prenume, String cnp, String dizabilitate){
        p = new Persoana(nume, prenume, cnp);
        //this.dizabilitate = dizabilitate != null ? dizabilitate : estePersoanaCuDizabilitati();
        this.varsta = calculeazaVarsta(cnp);
    }
    public Beneficiar(String nume, String prenume, String cnp, String serie, String numar, String judet, String localitate, String dizabilitate) {
        this.p = new Persoana(nume, prenume, cnp, serie, numar, judet, localitate);
        this.varsta = calculeazaVarsta(cnp);
        //this.dizabilitate = dizabilitate != null ? dizabilitate : estePersoanaCuDizabilitati();
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

    public String getCategoriaRisc() {
        if (varsta >= 65)
            return "Categoria a II-a A";
        return "Fără risc major";
    }
//    public String estePersoanaCuDizabilitati() {
//        return dizabilitate;
//    }
    public int getVarsta() {
        return varsta;
    }
    @Override
    public String toString() {
        return p.getNume() + " " + p.getPrenume() + ", CNP: " + p.getCNP() + ", varsta: " + varsta;// + ", risc: " + dizabilitate;
    }
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Beneficiar that = (Beneficiar) o;
        return p.getCNP().equals(that.p.getCNP());
    }
}
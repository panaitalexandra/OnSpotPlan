import java.util.Random;
/**
 *
 * @author Mihaila Alexia-Andreea
 */
public class Vaccin {
    private String nume;
    private int zilePanaLaRapel;

    public Vaccin(String nume) {
        this.nume = nume;
        this.zilePanaLaRapel = calculeazaZileRapel(nume);
    }
    public static Vaccin alegeVaccin() {
        String[] vaccinuri = {"Pfizer", "Moderna", "AstraZeneca"};
        int index = new Random().nextInt(vaccinuri.length);
        return new Vaccin(vaccinuri[index]);
    }
    private int calculeazaZileRapel(String nume) {
        return switch (nume.toLowerCase()) {
            case "astrazeneca" -> 56;
            case "pfizer" -> 21;
            case "moderna" -> 28;
            default -> 0;
        };
    }
    public String getNume() {
        return nume;
    }

    public int getZilePanaLaRapel() {
        return zilePanaLaRapel;
    }

    @Override
    public String toString() {
        return nume;
    }
}
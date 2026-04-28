/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.time.*;

public class Programare {
    private Beneficiar beneficiar;
    private String centruVaccinare;
    private LocalDate data;
    private LocalTime ora;
    private Vaccin tipVaccin; // AstraZeneca, Pfizer, Moderna
    private LocalDate dataRapel;

    public Programare(Beneficiar beneficiar, String centruVaccinare, LocalDate data, LocalTime ora, Vaccin tipVaccin) {
        this.beneficiar = beneficiar;
        this.centruVaccinare = centruVaccinare;
        this.data = data;
        this.ora = ora;
        this.tipVaccin = tipVaccin;
        this.dataRapel = calculeazaRapel(data, tipVaccin);
    }
    private LocalDate calculeazaRapel(LocalDate primaDoza, Vaccin tipVaccin) {
        int zile = tipVaccin.getZilePanaLaRapel();
        return zile > 0 ? primaDoza.plusDays(zile) : null;
    }    
    
    public Beneficiar getBeneficiar() {
        return beneficiar;
    }
    public LocalDate getData() {
        return data;
    }
    public LocalTime getOra() {
        return ora;
    }
    public String getCentruVaccinare() {
        return centruVaccinare;
    }

    @Override
    public String toString() {
        return "Programare pentru " + beneficiar.getPersoana().getNume() + " " + beneficiar.getPersoana().getPrenume() +
               "\nCentrul: " + centruVaccinare +
               "\nData: " + data + " la ora " + ora +
               "\nVaccin: " + tipVaccin +
               "\nRapel: " + (dataRapel != null ? dataRapel : "N/A");
    }

    public String toFileString() {
        return beneficiar.getPersoana().getNume() + ";" +
                beneficiar.getPersoana().getPrenume() + ";" +
                beneficiar.getPersoana().getCNP() + ";" +
                centruVaccinare + ";" +
                data.toString() + ";" +
                ora.toString() + ";" +
                tipVaccin.toString();
    }
}


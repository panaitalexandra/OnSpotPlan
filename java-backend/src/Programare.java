/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.time.*;

public class Programare {
    private Client beneficiar;
    private Event eveniment;
    private LocalDate data;
    private LocalTime ora;
    private Bilet bilet;

    public Programare(Client beneficiar, Event eveniment, LocalDate data, LocalTime ora, Bilet bilet) {
        this.beneficiar = beneficiar;
        this.eveniment = eveniment;
        this.data = data;
        this.ora = ora;
        this.bilet = bilet;
    }
    public Client getBeneficiar() {
        return beneficiar;
    }

    public String getEveniment() {
        return eveniment.getNume();
    }

    public LocalDate getData() {
        return data;
    }

    public LocalTime getOra() {
        return ora;
    }

    public Bilet getBilet() {
        return bilet;
    }

    @Override
    public String toString() {
        return "Rezervare Eveniment: " + getEveniment() +
                "\nParticipant: " + beneficiar.getPersoana().getNume() + " " + beneficiar.getPersoana().getPrenume() +
                "\nData: " + data + " la ora " + ora +
                "\nTip Bilet: " + bilet.getTip();
    }

    public String toFileString() {
        Persoana p = beneficiar.getPersoana();
        return String.join(";",
                p.getNume(),
                p.getPrenume(),
                p.getCNP(),
                beneficiar.getTelefon(),
                getEveniment(),
                data.toString(),
                ora.toString(),
                bilet.getTip()
        );
    }
}


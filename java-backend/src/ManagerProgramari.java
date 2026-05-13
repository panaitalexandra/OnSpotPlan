/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.io.*;
import java.time.*;
import java.util.*;

public class ManagerProgramari {
    private List<Programare> programari;
    private static ManagerProgramari instanta;

    private ManagerProgramari() {
        programari = new ArrayList<>();
        citesteDinFisier();
    }
    public static ManagerProgramari getInstance() {
        if (instanta == null) {
            instanta = new ManagerProgramari();
        }
        return instanta;
    }

    public boolean adaugaProgramare(Programare p) {
        String cnpNou = p.getBeneficiar().getPersoana().getCNP();
        String numeEvNou = p.getEveniment();

        for (Programare existent : programari) {
            String cnpExistent = existent.getBeneficiar().getPersoana().getCNP();
            String numeEvExistent = existent.getEveniment();

            if (cnpExistent.equals(cnpNou) &&
                    numeEvExistent.equals(numeEvNou) &&
                    existent.getData().equals(p.getData()) &&
                    existent.getOra().equals(p.getOra()))
                return false;
        }

        programari.add(p);
        scrieInFisier();
        return true;
    }

    public boolean stergeProgramare(Client b) {
        boolean modificat = false;
        Iterator<Programare> it = programari.iterator();
        while (it.hasNext()) {
            Programare p = it.next();
            if (p.getBeneficiar().equals(b)) {
                it.remove();
                modificat = true;
            }
        }
        if (modificat)
            scrieInFisier();
        return modificat;
    }

    public List<Programare> getProgramariPentruBeneficiar(Client b) {
        List<Programare> rez = new ArrayList<>();
        for (Programare p : programari)
            if (p.getBeneficiar().equals(b))
                rez.add(p);
        return rez;
    }

    private void citesteDinFisier() {
        File f = new File("events_booked.txt");
        if (!f.exists()) return;

        try (BufferedReader br = new BufferedReader(new FileReader(f))) {
            String linie;
            while ((linie = br.readLine()) != null) {
                String[] parti = linie.split(";");
                if (parti.length == 8) {
                    String nume = parti[0];
                    String prenume = parti[1];
                    String cnp = parti[2];
                    String telefon = parti[3];
                    String numeEv = parti[4];
                    LocalDate data = LocalDate.parse(parti[5]);
                    LocalTime ora = LocalTime.parse(parti[6]);
                    String tipBilet = parti[7];

                    Client b = new Client(nume, prenume, cnp, telefon);
                    Event ev = new Event("N/A", numeEv, "Loaded from history", "N/A", "N/A", "N/A", 0.0);
                    Bilet t = new Bilet(tipBilet);
                    Programare p = new Programare(b, ev, data, ora, t);

                    programari.add(p);
                }
            }
        } catch (Exception e) {
            System.out.println("Eroare la incarcarea fisierului: " + e.getMessage());
        }
    }

    private void scrieInFisier() {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter("events_booked.txt"))) {
            for (Programare p : programari) {
                Persoana pers = p.getBeneficiar().getPersoana();
                String linie = String.join(";",
                        pers.getNume(),
                        pers.getPrenume(),
                        pers.getCNP(),
                        p.getBeneficiar().getTelefon(),
                        p.getEveniment(),
                        p.getData().toString(),
                        p.getOra().toString(),
                        p.getBilet().getTip()
                );
                bw.write(linie);
                bw.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}


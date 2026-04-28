/**
 *
 * @author Mihaila ALexia-Andreea
 */
import java.io.*;
import java.time.*;
import java.util.*;

public class ManagerProgramari {
    private List<Programare> programari;

    public ManagerProgramari() {
        programari = new ArrayList<>();
        citesteDinFisier();
    }

    public boolean adaugaProgramare(Programare p) {
        for (Programare prog : programari)
            if (prog.getBeneficiar().equals(p.getBeneficiar()) &&
                    prog.getData().equals(p.getData()) &&
                    prog.getOra().equals(p.getOra()))
                return false;

        programari.add(p);
        scrieInFisier();
        return true;
    }

    public boolean stergeProgramare(Beneficiar b) {
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

    public List<Programare> getProgramariPentruBeneficiar(Beneficiar b) {
        List<Programare> rez = new ArrayList<>();
        for (Programare p : programari)
            if (p.getBeneficiar().equals(b))
                rez.add(p);
        return rez;
    }

    private void citesteDinFisier() {
        File f = new File("programari.txt");
        if (!f.exists()) return;

        try (BufferedReader br = new BufferedReader(new FileReader(f))) {
            String linie;
            while ((linie = br.readLine()) != null) {
                // Format: nume;prenume;cnp;data;ora;centru
                String[] parti = linie.split(";");
                if (parti.length == 7) {
                    String nume = parti[0];
                    String prenume = parti[1];
                    String cnp = parti[2];
                    String centru = parti[3];
                    LocalDate data = LocalDate.parse(parti[4]);
                    LocalTime ora = LocalTime.parse(parti[5]);
                    String vaccin = parti[6];

                    Beneficiar b = new Beneficiar(nume, prenume, cnp, null);
                    Vaccin tipVaccin = new Vaccin(vaccin);
                    Programare p = new Programare(b, centru, data, ora, tipVaccin);
                    programari.add(p);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void scrieInFisier() {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter("programari.txt"))) {
            for (Programare p : programari) {
                bw.write(p.toFileString());
                bw.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}


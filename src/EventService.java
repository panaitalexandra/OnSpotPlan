import java.util.*;
import java.io.*;

public class EventService {
    private static EventService instanta;

    private EventService() {}

    public static EventService getInstance() {
        if (instanta == null) instanta = new EventService();
        return instanta;
    }

    public List<String> getLocatiiDupaJudet(String judet) {
        List<String> locatii = new ArrayList<>();
        String numeFisier = "events_" + judet + ".txt";
        File f = new File(numeFisier);

        if (f.exists()) {
            try (BufferedReader br = new BufferedReader(new FileReader(f))) {
                String linie;
                while ((linie = br.readLine()) != null) {
                    locatii.add(linie.trim());
                }
            } catch (IOException e) { e.printStackTrace(); }
        }
        return locatii;
    }

    public boolean inregistreazaInteres(String nume, String prenume, String locatie) {
        try (FileWriter fw = new FileWriter("listaAsteptare.txt", true);
             BufferedWriter bw = new BufferedWriter(fw)) {
            bw.write(nume + ";" + prenume + ";" + locatie);
            bw.newLine();
            return true;
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
    }
}
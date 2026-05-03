import java.util.*;
import java.io.*;

/**
 *
 * @author Panait Claudia-Alexandra
 */
public class ManagerClienti {
    private ArrayList<Client> clienti;
    private String fisier;
    private static Map<String, ManagerClienti> instante = new HashMap<>();

    private ManagerClienti(String userId) {
        clienti = new ArrayList<>();
        this.fisier = "beneficiari_" + userId + ".txt";
        incarcaDinFisier();
    }
    private void incarcaDinFisier() {
        File f = new File(fisier);
        if (!f.exists()) {
            try {
                f.createNewFile();
            } catch (IOException e) { e.printStackTrace();}
            return;
        }
        try (BufferedReader br = new BufferedReader(new FileReader(f))) {
            String linie;
            while ((linie = br.readLine()) != null) {
                String[] parts = linie.split("_");

                if (parts.length == 8) {
                    Client b = new Client(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7]);
                    clienti.add(b);
                }

                else if (parts.length == 7) {
                    Client c = new Client(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], "Nespecificat");
                    clienti.add(c);
                }
            }
        } catch (IOException e) { e.printStackTrace(); }
    }

    public boolean adaugaBeneficiar(Client b) {
        clienti.add(b);
        salveaza();
        return true;
    }
    public boolean poateAdaugaBeneficiar() {
        return clienti.size() < 10;
    }

    public void salveaza() {
        try (PrintWriter pw = new PrintWriter(new FileWriter(fisier))) {
            for (Client b : clienti)
                pw.println(String.join("_",
                        b.getPersoana().getNume(),
                        b.getPersoana().getPrenume(),
                        b.getPersoana().getCNP(),
                        b.getPersoana().getCarteIdentitate().getSerie(),
                        b.getPersoana().getCarteIdentitate().getNumar(),
                        b.getPersoana().getCarteIdentitate().getJudet(),
                        b.getPersoana().getCarteIdentitate().getLocalitate(),
                        b.getTelefon()
                ));
        } catch (IOException e) { e.printStackTrace(); }
    }
    public ArrayList<Client> getLista() {
        return clienti;
    }

    public static ManagerClienti getInstance(String userId) {
        if (!instante.containsKey(userId)) {
            instante.put(userId, new ManagerClienti(userId));
        }
        return instante.get(userId);
    }
}

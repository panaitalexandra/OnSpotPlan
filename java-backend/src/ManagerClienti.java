/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.util.*;
import java.io.*;

public class ManagerClienti {
    private ArrayList<Client> clienti;
    private String fisier;
    private static Map<String, ManagerClienti> instante = new HashMap<>();

    private ManagerClienti(String userId) {
        clienti = new ArrayList<>();
        this.fisier = "client_" + userId + ".txt";
        incarcaDinFisier();
    }

    private void incarcaDinFisier() {
        File f = new File(fisier);
        if (!f.exists()) {
            try { f.createNewFile(); } catch (IOException e) { e.printStackTrace(); }
            return;
        }

        try (BufferedReader br = new BufferedReader(new FileReader(f))) {
            String linie;
            while ((linie = br.readLine()) != null) {
                String[] parts = linie.split("_");
                if (parts.length == 6) {
                    clienti.add(new Client(parts[0], parts[1], parts[2], "N/A", "N/A", parts[3], parts[4], parts[5]));
                }
            }
        } catch (IOException e) { e.printStackTrace(); }
    }

    public boolean adaugaClient(Client c) {
        clienti.add(c);
        salveaza();
        return true;
    }
    public boolean stergeClient(int index) {
        if (index >= 0 && index < clienti.size()) {
            clienti.remove(index); // Stergem din memoria RAM (ArrayList)
            salveaza();            // Actualizam fisierul .txt ca sa ramana sters si la repornire
            return true;
        }
        return false;
    }
    public void salveaza() {
        try (PrintWriter pw = new PrintWriter(new FileWriter(fisier))) {
            for (Client c : clienti) {
                Persoana p = c.getPersoana();
                pw.println(String.join("_",
                        p.getNume(),
                        p.getPrenume(),
                        p.getCNP(),
                        p.getCarteIdentitate().getRegion(),
                p.getCarteIdentitate().getCity(),
                c.getTelefon()
                ));
            }
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
    public boolean actualizeazaClient(int index, Client c) {
        if (index >= 0 && index < clienti.size()) {
            clienti.set(index, c);
            salveaza();
            return true;
        }
        return false;
    }
}
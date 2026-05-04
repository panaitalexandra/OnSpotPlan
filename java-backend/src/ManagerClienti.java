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
                // Verificăm structura: Nume, Prenume, CNP, Judet, Localitate, Telefon (6 câmpuri)
                if (parts.length == 6) {
                    // Folosim Constructorul 2 al clasei Client, punem "N/A" pentru Serie/Numar
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

    public void salveaza() {
        try (PrintWriter pw = new PrintWriter(new FileWriter(fisier))) {
            for (Client c : clienti) {
                Persoana p = c.getPersoana();
                // Salvăm atributele esențiale separate prin "_"[cite: 10]
                pw.println(String.join("_",
                        p.getNume(),
                        p.getPrenume(),
                        p.getCNP(),
                        p.getCarteIdentitate().getJudet(),
                p.getCarteIdentitate().getLocalitate(),
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
}
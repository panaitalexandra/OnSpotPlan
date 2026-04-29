import java.util.*;
import java.io.*;
import javax.swing.*;
/**
 *
 * @author Panait Claudia-Alexandra
 */
public class ManagerBeneficiari {
    private ArrayList<Beneficiar> beneficiari;
    private String fisier;
    private static Map<String, ManagerBeneficiari> instante = new HashMap<>();

    private ManagerBeneficiari(String userId) {
        beneficiari = new ArrayList<>();
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
                    Beneficiar b = new Beneficiar(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7]);
                    beneficiari.add(b);
                }
            }
        } catch (IOException e) { e.printStackTrace(); }
    }

    public boolean adaugaBeneficiar(Beneficiar b) {
        beneficiari.add(b);
        salveaza();
        return true;
    }
    public boolean poateAdaugaBeneficiar() {
        return beneficiari.size() < 10;
    }

    public void salveaza() {
        try (PrintWriter pw = new PrintWriter(new FileWriter(fisier))) {
            for (Beneficiar b : beneficiari)
                pw.println(String.join("_",
                        b.getPersoana().getNume(),
                        b.getPersoana().getPrenume(),
                        b.getPersoana().getCNP(),
                        b.getPersoana().getCarteIdentitate().getSerie(),
                        b.getPersoana().getCarteIdentitate().getNumar(),
                        b.getPersoana().getCarteIdentitate().getJudet(),
                        b.getPersoana().getCarteIdentitate().getLocalitate()
                        //b.estePersoanaCuDizabilitati()
                ));
        } catch (IOException e) { e.printStackTrace(); }
    }
    public ArrayList<Beneficiar> getLista() {
        return beneficiari;
    }

    public static ManagerBeneficiari getInstance(String userId) {
        if (!instante.containsKey(userId)) {
            instante.put(userId, new ManagerBeneficiari(userId));
        }
        return instante.get(userId);
    }
}

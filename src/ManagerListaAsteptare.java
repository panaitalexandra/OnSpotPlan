/**
 *
 * @author Mihaila ALexia-Andreea
 */
import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ManagerListaAsteptare {
    private static ManagerListaAsteptare instance = new ManagerListaAsteptare();
    private Map<String, List<Beneficiar>> listeAsteptare;

    public ManagerListaAsteptare() {
        this.listeAsteptare = new HashMap<>();
    }
    public static ManagerListaAsteptare getInstance() {
        return instance;
    }
    public void adaugaBeneficiar(String numeCentru, Beneficiar b) {
        listeAsteptare.putIfAbsent(numeCentru, new ArrayList<>());
        listeAsteptare.get(numeCentru).add(b);
    }

    public void stergeBeneficiar(String numeCentru, String cnp) {
        List<Beneficiar> lista = listeAsteptare.get(numeCentru);
        if (lista != null)
            lista.removeIf(b -> b.getPersoana().getCNP().equals(cnp));
    }
    public void incarcaDinFisier(String numeFisier) {
        listeAsteptare.clear();
        File f = new File(numeFisier);
        if (!f.exists()) return;

        try (BufferedReader br = new BufferedReader(new FileReader(f))) {
            String linie;
            while ((linie = br.readLine()) != null) {
                String[] parti = linie.split(";");
                if (parti.length >= 4) {
                    String nume = parti[0].trim();
                    String prenume = parti[1].trim();
                    String cnp = parti[2].trim();
                    String centru = parti[3].trim();

                    Beneficiar b = new Beneficiar(nume, prenume, cnp, null);
                    adaugaBeneficiar(centru, b);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public List<String> getCentre() {
        return new ArrayList<>(listeAsteptare.keySet());
    }

    public boolean esteInLista(String numeCentru, String cnp) {
        List<Beneficiar> lista = listeAsteptare.get(numeCentru);
        if (lista == null) return false;
        return lista.stream().anyMatch(b -> b.getPersoana().getCNP().equals(cnp));
    }
    public void salveazaInFisier(String numeFisier) {
        try (PrintWriter pw = new PrintWriter(numeFisier)) {
            for (String centru : listeAsteptare.keySet()) {
                for (Beneficiar b : listeAsteptare.get(centru)) {
                    pw.println(b.getPersoana().getNume() + ";" +
                            b.getPersoana().getPrenume() + ";" +
                            b.getPersoana().getCNP() + ";" +
                            centru);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

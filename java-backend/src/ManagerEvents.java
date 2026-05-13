import java.util.ArrayList;
import java.util.List;

public class ManagerEvents {
    private List<Event> listaEvenimente;
    private static ManagerEvents instanta;

    private ManagerEvents() {
        listaEvenimente = new ArrayList<>();
        // Populare de test - Asigură-te că id-urile și datele sunt corecte
        listaEvenimente.add(new Event("1", "Concert Rock", "O seară de rock alternativ.", "Constanta", "Portul Tomis", "resources/ev1.jpg", 150.0));
        listaEvenimente.add(new Event("2", "Festival Tech", "Prezentări despre ultimele inovații.", "Bucuresti", "Romexpo", "resources/ev3.jpg", 0.0));
    }

    public static ManagerEvents getInstance() {
        if (instanta == null) instanta = new ManagerEvents();
        return instanta;
    }

    // Aceasta este metoda pe care o va apela Python
    public String getDescriereLocatie(String numeEveniment) {
        for (Event e : listaEvenimente) {
            if (e.getNume().equalsIgnoreCase(numeEveniment)) {
                return e.getDescriereLocatie(); // Returnează descrierea din obiectul Event găsit
            }
        }
        return "Descriere indisponibilă pentru: " + numeEveniment;
    }

    public List<Event> getToateEvenimentele() {
        return listaEvenimente;
    }
}
import java.io.Serializable;

public class TicketCategories implements Serializable {
    private int id; // Corespunde cu 'id' din tabela 'categorie_bilete'
    private String tipBilet; // VIP, Standard, etc.
    private double pret;

    public TicketCategories(int id, String tipBilet, double pret) {
        this.id = id;
        this.tipBilet = tipBilet;
        this.pret = pret;
    }

    public int getId() { return id; }
    public String getTicketType() { return tipBilet; }
    public double getPrice() { return pret; }

    @Override
    public String toString() {
        return tipBilet + " - " + pret + " RON";
    }
}
/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.io.Serializable;

public class Ticket implements Serializable {
    private int idBilet;
    private String serie;
    private int numar;

    public Ticket(int idBilet, String serie, int numar) {
        this.idBilet = idBilet;
        this.serie = serie;
        this.numar = numar;
    }

    public int getIdBilet() { return idBilet; }
    public String getSerie() { return serie; }
    public int getNumar() { return numar; }
}
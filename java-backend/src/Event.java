import java.io.Serializable;

public class Event implements Serializable {
    private String id;
    private String nume;
    private String descriere;
    private String regiune;
    private String locatieSpecifica;
    private String caleImagine;
    private double pretBilet;

    public Event(String id, String nume, String descriere, String regiune, String locatieSpecifica, String caleImagine, double pretBilet) {
        this.id = id;
        this.nume = nume;
        this.descriere = descriere;
        this.regiune = regiune;
        this.locatieSpecifica = locatieSpecifica;
        this.caleImagine = caleImagine;
        this.pretBilet = pretBilet;
    }

    public String getNume() { return nume; }
    public String getDescriereLocatie() { return descriere; }
    public String getRegiune() { return regiune; }
    public String getLocatieSpecifica() { return locatieSpecifica; }
    public String getCaleImagine() { return caleImagine; }
    public double getPretBilet() { return pretBilet; }
}
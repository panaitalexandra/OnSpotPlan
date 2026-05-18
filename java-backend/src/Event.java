import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

public class Event implements Serializable {
    private int id;
    private String name;
    private String description;
    private String type;
    private String location;
    private String dateTime;
    private String city;
    private List<TicketCategories> ticketCategories;
    private String imagePath = "resources/placeholder.jpg";

    public String getCaleImagine() {
        return imagePath;
    }

    public Event(int id, String name, String description, String type, String locationInfo, String dateTimeInfo, String city) {        this.id = id;
        this.name = name;
        this.description = description;
        this.type = type;
        this.location = locationInfo;
        this.dateTime = dateTimeInfo;
        this.city = city;
        this.ticketCategories = new ArrayList<>();
    }

    public void addCategory(TicketCategories tc) {
        this.ticketCategories.add(tc);
    }
    public int getId() { return id; }
    public String getName() { return name; }
    public String getDescription() { return description; }
    public String getType() { return type; }
    public String getLocation() { return location; }
    public String getDateTime() { return dateTime; }
    public String getCity() { return city; }
    public List<TicketCategories> getTicketCategories() { return ticketCategories; }
    public String getImagePath() { return imagePath; }
}
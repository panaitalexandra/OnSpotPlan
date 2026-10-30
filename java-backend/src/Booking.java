/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.time.*;

public class Booking {
    private Profile profile;
    private Event event;
    private LocalDate date;
    private LocalTime time;
    private TicketCategories category;
    private String status;
    private String confirmation;

    public Booking(Profile profile, Event event, LocalDate date, LocalTime time, TicketCategories category, String status, String confirmation) {
        this.profile = profile;
        this.event = event;
        this.date = date;
        this.time = time;
        this.category = category;
        this.status = status;
        this.confirmation = confirmation;
    }
    public Profile getProfile() { return profile; }
    public Event getEvent() { return event; }
    public TicketCategories getCategory() { return category; }
    public LocalDate getDate() { return date; }
    public LocalTime getTime() { return time; }
    public String getStatus() { return status; }
    public String getConfirmation() { return confirmation; }
    public void setConfirmation(String confirmation) { this.confirmation = confirmation; }

}


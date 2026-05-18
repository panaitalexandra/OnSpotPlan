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

    public Booking(Profile profile, Event event, LocalDate date, LocalTime time, TicketCategories category) {
        this.profile = profile;
        this.event = event;
        this.date = date;
        this.time = time;
        this.category = category;
    }
    public Profile getProfile() { return profile; }
    public Event getEvent() { return event; }
    public TicketCategories getCategory() { return category; }
    public LocalDate getDate() { return date; }
    public LocalTime getTime() { return time; }

    public String getEvenimentNume() { return event.getName(); }

//    @Override
//    public String toString() {
//        return "Rezervare Eveniment: " + getEvenimentNume() +
//                "\nParticipant: " + profile.getPerson().getLast_name() + " " + profile.getPerson().getFirst_name() +
//                "\nData: " + data + " la ora " + ora +
//                "\nCategorie Ticket: " + categorieAleasa.getTipBilet() + " (" + categorieAleasa.getPrice() + " RON)";
//    }
}


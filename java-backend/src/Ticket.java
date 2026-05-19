/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.io.Serializable;

public class Ticket implements Serializable {
    private int ticketId;
    private String ticketSeries;
    private int ticketNumber;

    public Ticket(int ticketId, String TicketSeries, int TicketNumber) {
        this.ticketId = ticketId;
        this.ticketSeries = TicketSeries;
        this.ticketNumber = TicketNumber;
    }

    public int getTicketId() { return ticketId; }
    public String getTicketSeries() { return ticketSeries; }
    public int getTicketNumber() { return ticketNumber; }
}
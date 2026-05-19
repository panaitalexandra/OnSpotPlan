import java.io.Serializable;

public class TicketCategories implements Serializable {
    private int ticketId;
    private String ticketCategory;
    private double ticketPrice;

    public TicketCategories(int ticketId, String ticketCategory, double ticketPrice) {
        this.ticketId = ticketId;
        this.ticketCategory = ticketCategory;
        this.ticketPrice = ticketPrice;
    }

    public int getTicketId() { return ticketId; }
    public String getTicketType() { return ticketCategory; }
    public double getPrice() { return ticketPrice; }

    @Override
    public String toString() {
        return ticketCategory + " - " + ticketPrice + " RON";
    }
}
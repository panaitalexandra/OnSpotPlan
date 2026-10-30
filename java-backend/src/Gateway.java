/**
 *
 * @author Panait Claudia-Alexandra
 */
import py4j.GatewayServer;

public class Gateway {
    public UserManager getUserManager() {
        return UserManager.getInstance();
    }
    public ProfileManager getProfileManager(String email) {
        int userId = UserManager.getInstance().getIdByEmail(email);
        return ProfileManager.getInstance(userId);
    }
    public EventService getEventService() {
        return EventService.getInstance();
    }
    public EventManager getEventManager() {
        return EventManager.getInstance();
    }
    public BookingManager getBookingManager(int userId) {
        return BookingManager.getInstance(userId);
    }

    public static void main(String[] args) {
        GatewayServer server = new GatewayServer(new Gateway());
        server.start();
        System.out.println("Java is on - run py");
    }
}
/**
 *
 * @author Panait Claudia-Alexandra
 */
import py4j.GatewayServer;

public class Gateway {
    public ManagerUtilizatori getManagerUtilizatori() {
        return ManagerUtilizatori.getInstance();
    }
    public ManagerClienti getManagerClienti(String userId) {
        return ManagerClienti.getInstance(userId);
    }
    public EventService getLocatieService() {
        return EventService.getInstance();
    }
    public static void main(String[] args) {
        GatewayServer server = new GatewayServer(new Gateway());
        server.start();
        System.out.println("Java server is ON. Run Python!");
    }
}


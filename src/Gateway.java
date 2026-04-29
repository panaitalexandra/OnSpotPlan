import py4j.GatewayServer;

public class Gateway {
    public ManagerUtilizatori getManagerUtilizatori() {
        return ManagerUtilizatori.getInstance();
    }
    public String test() {
        return "legatura stabilita";
    }
    public static void main(String[] args) {
        GatewayServer server = new GatewayServer(new Gateway());
        server.start();
        System.out.println("Serverul Java a pornit. Python se poate conecta!");
    }
}


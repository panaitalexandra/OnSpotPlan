import py4j.GatewayServer;

public class Gateway {
    private ManagerProgramari manager = new ManagerProgramari();

    public ManagerProgramari getManager() {
        return manager;
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


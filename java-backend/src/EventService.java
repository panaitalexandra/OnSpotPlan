/**
 *
 * @author Panait Claudia-Alexandra
 */
public class EventService {
    private static EventService instanta;

    private EventService() {}

    public static EventService getInstance() {
        if (instanta == null)
            instanta = new EventService();
        return instanta;
    }
}
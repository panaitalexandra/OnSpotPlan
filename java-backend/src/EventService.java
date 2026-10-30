/**
 *
 * @author Panait Claudia-Alexandra
 */
public class EventService {
    private static EventService instance;

    private EventService() {}

    public static EventService getInstance() {
        if (instance == null)
            instance = new EventService();
        return instance;
    }
}
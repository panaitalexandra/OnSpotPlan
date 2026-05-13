/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.util.regex.Pattern;

public class ValidatorEmail {
    /**
     * ^[a-zA-Z0-9._%+-]+  -> Acceptă litere, cifre și simboluri comune înainte de @
     * @                   -> Obligatoriu simbolul @
     * [a-zA-Z0-9.-]+      -> Acceptă orice domeniu (ex: gmail, outlook, firma-mea, proton, etc.)
     * \\.[a-zA-Z]{2,}$    -> Acceptă orice extensie de minim 2 litere (ex: .ro, .com, .net, .org, .edu, etc.)
     */
    private static final String EMAIL_PATTERN = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$";

    public static boolean esteValid(String email) {
        if (email == null || email.isEmpty()) {
            return false;
        }
        // Pattern.matches verifică tot string-ul și nu dă crash pe input-uri scurte
        return Pattern.matches(EMAIL_PATTERN, email);
    }
}
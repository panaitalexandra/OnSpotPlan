/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.util.regex.Pattern;

public class EmailValidation {
    /**
     * ^[a-zA-Z0-9._%+-]+  -> litere, cifre si semne obisnuite inainte de @
     * @                   -> obligatoriu
     * [a-zA-Z0-9.-]+      -> domeniul
     * \\.[a-zA-Z]{2,}$    -> punct si extensia de minim doua litere
     */
    private static final String EMAIL_PATTERN = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$";

    public static boolean isValid(String email) {
        if (email == null || email.isEmpty()) {
            return false;
        }
        return Pattern.matches(EMAIL_PATTERN, email);
    }
}
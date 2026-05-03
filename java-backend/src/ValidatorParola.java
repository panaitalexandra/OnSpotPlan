/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.util.regex.Pattern;

public class ValidatorParola {
    // (?=.*[0-9]) -> cel puțin o cifră[cite: 3]
    // (?=.*[a-z]) -> cel puțin o minusculă[cite: 3]
    // (?=.*[A-Z]) -> cel puțin o majusculă[cite: 3]
    // (?=.*[#$*]) -> cel puțin un simbol din setul tău (#, $, *)[cite: 3]
    // .{8,}       -> lungime minimă 8[cite: 3]
    private static final String PASSWORD_PATTERN =
            "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[#$*]).{8,}$";

    public static boolean esteValida(String parola) {
        if (parola == null) return false;
        return Pattern.matches(PASSWORD_PATTERN, parola);
    }
}
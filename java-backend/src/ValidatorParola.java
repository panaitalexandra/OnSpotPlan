/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.util.regex.Pattern;

public class ValidatorParola {
    public static boolean areLungimeMinima(String parola) {
        return parola != null && parola.length() >= 8;
    }

    public static boolean areMajuscula(String parola) {
        return parola != null && parola.matches(".*[A-Z].*");
    }

    public static boolean areCifra(String parola) {
        return parola != null && parola.matches(".*[0-9].*");
    }

    public static boolean areCaracterSpecial(String parola) {
        return parola != null && parola.matches(".*[!#$%^*].*");
    }
    public static boolean esteValida(String parola) {
        return areLungimeMinima(parola) && areMajuscula(parola) &&
                areCifra(parola) && areCaracterSpecial(parola);
    }
}

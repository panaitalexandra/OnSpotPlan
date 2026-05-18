/**
 *
 * @author Panait Claudia-Alexandra
 */

public class PasswordValidation {
    public static boolean hasMinLength(String parola) {
        return parola != null && parola.length() >= 8;
    }

    public static boolean containsUppercase(String parola) {
        return parola != null && parola.matches(".*[A-Z].*");
    }

    public static boolean containsNum(String parola) {
        return parola != null && parola.matches(".*[0-9].*");
    }

    public static boolean containsSpecial(String parola) {
        return parola != null && parola.matches(".*[!#$%^*].*");
    }
    public static boolean validation(String parola) {
        return hasMinLength(parola) && containsUppercase(parola) &&
                containsNum(parola) && containsSpecial(parola);
    }
}

/**
 *
 * @author Panait Claudia-Alexandra
 */
public class ValidatorParola {
    public static boolean esteValida(String parola) {
        if (parola.length() < 8)
            return false;

        boolean contineLiteraMare = false;
        boolean contineLiteraMica = false;
        boolean contineCifra = false;
        boolean contineSimbol = false;

        for (int i = 0; i < parola.length(); i++) {
            char c = parola.charAt(i);
            if (Character.isUpperCase(c)) contineLiteraMare = true;
            if (Character.isLowerCase(c)) contineLiteraMica = true;
            if (Character.isDigit(c))     contineCifra = true;
            if (c == '#' || c == '$' || c == '*') contineSimbol = true;
        }

        // Regulile impuse
        if (!contineLiteraMare) return false;               
        if (!contineLiteraMica) return false;              
        if (!contineCifra) return false;                  
        if (!contineSimbol) return false;                  

        return true;
    }
}

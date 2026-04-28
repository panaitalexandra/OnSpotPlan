/**
 *
 * @author Mihaila Alexia-Andreea
 */
public class ValidatorEmail {
        public static boolean esteValid(String email) {
            boolean contineGmailYahoo = false;
            boolean contineAr = false; //@
            boolean continePct = false;
            boolean contineCom = false;

            for (int i = 0; i < email.length(); i++) {
                char c = email.charAt(i);
                if (c == '@') contineAr = true;
                if (c == '.') continePct = true;
            }
            String b ,d;
            if(contineAr == continePct == true) {
                b = email.substring(email.indexOf("@") + 1, email.indexOf(".") );//aici pun gmail sau yahoo
                d = email.substring(email.indexOf(".") + 1);// aici pun com sau ro
                if (b.equals("gmail") || b.equals("yahoo")) contineGmailYahoo = true;
                if (d.equals("com") || d.equals("ro")) contineCom = true;
                if (contineGmailYahoo == contineCom == true)   return true;
            }
            return false;
        }
}

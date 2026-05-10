/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.io.*;
import java.util.*;

public class ManagerUtilizatori {
    private ArrayList<Utilizator> users;
    private static ManagerUtilizatori instanta;
    
    private ManagerUtilizatori(){
        users = new ArrayList<>();
        File f = new File("conturiUtilizatori.txt");
        
        if(f.exists()){
            try (BufferedReader br = new BufferedReader(new FileReader(f))) {
                String line;
                String[] arr;
                        
                while ((line = br.readLine()) != null) {
                    arr = line.split("\\|");
                   try {
                        Utilizator user;
                        if (arr.length == 2) 
                            user = new Utilizator(arr[0], arr[1]);
                        else if (arr.length == 10)
                                    user = new Utilizator(arr[0], arr[1], arr[2], arr[3], 
                                    arr[4], arr[5], arr[6], arr[7], arr[8], arr[9]);
                                else 
                                    continue;
                            users.add(user);
                    }catch(Exception e){ e.printStackTrace(); }
                }
                br.close();
            }catch(IOException e){ e.printStackTrace(); }
        
        }
    }
    public boolean isEmailValid(String email) {
        return ValidatorEmail.esteValid(email);
    }

    public boolean isEmailRegistered(String email) {
        for (Utilizator user : users) {
            // Presupunem că Utilizator are getEmail()
            if (user.getEmail().equalsIgnoreCase(email.trim())) {
                return true;
            }
        }
        return false;
    }
    public boolean isParolaValida(String parola) {
        return ValidatorParola.areLungimeMinima(parola) &&
                ValidatorParola.areMajuscula(parola) &&
                ValidatorParola.areCifra(parola) &&
                ValidatorParola.areCaracterSpecial(parola);
    }

    public Utilizator inregistreazaUtilizator(String email, String parola) {
        // Verificăm formatul email-ului
        if (!isEmailValid(email)) return null;

        // Verificăm dacă email-ul e deja luat
        if (isEmailRegistered(email)) return null;

        // Verificăm întreaga structură a parolei
        if (!isParolaValida(parola)) return null;

        var user = new Utilizator(email, parola);
        users.add(user);
        salveaza(user);
        return user;
    }
    
    public Utilizator getUtilizator(String email, String parola){
        for(Utilizator user: users)
            if(user.autentificare(email, parola))
                return user;
        return null;
    }
    
    public void salveaza(Utilizator userNou){
        try{
            var bw = new PrintWriter(new FileWriter("conturiUtilizatori.txt", true));
            bw.println(userNou.toString());
            bw.close();
        }catch(IOException e){ e.printStackTrace(); }
    }
    
    public static ManagerUtilizatori getInstance(){
        if(instanta == null)
            instanta = new ManagerUtilizatori();
        return instanta;
    }
}
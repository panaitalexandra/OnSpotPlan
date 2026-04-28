/**
 *
 * @author Panait Claudia-Alexandra
 */
import java.io.*;
import java.util.*;
import javax.swing.*;

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
                        else if (arr.length == 9)
                                    user = new Utilizator(arr[0], arr[1], arr[2], arr[3], 
                                    arr[4], arr[5], arr[6], arr[7], arr[8]);
                                else 
                                    continue; // linie corupta
                            users.add(user);
                    }catch(Exception e){ e.printStackTrace(); }
                }
                br.close();
            }catch(IOException e){ e.printStackTrace(); }
        
        }
    }
    public Utilizator inregistreazaUtilizator(String email, String parola){
        if (!ValidatorEmail.esteValid(email)) {
            JOptionPane.showMessageDialog(null, "Email invalid!");
            return null;
        }
        if (!ValidatorParola.esteValida(parola)) {
            JOptionPane.showMessageDialog(null, """
                                                Parola trebuie să conțină cel puțin 8 caractere dintre care:
                                                - o majusculă
                                                - o minusculă
                                                - o cifra
                                                - un caracter special: #, $, * """);
            return null;
        }    
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
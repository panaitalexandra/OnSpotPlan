/**
 *
 * @author Panait Claudia-Alexandra
 */
public class CredentialeUtilizator {
    private static CredentialeUtilizator instanta;
    private String user, password;
    
    public void setUser(String user, String password){
        this.user = user;
        this.password = password;
    }
    public String getUser(){
        return user;
    }
    public static CredentialeUtilizator getInstance(){
        if(instanta == null)
            instanta = new CredentialeUtilizator();
        return instanta;
    }
}

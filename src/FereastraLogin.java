import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
/**
 *
 * @author Panait Claudia-Alexandra
 */
public class FereastraLogin extends JFrame {
    private JFrame f;
    private JLabel lUser, lPassword;
    private JTextField tUser;
    private JPasswordField tPassword;
    private JButton bLogin, bSignup;
    private ManagerUtilizatori managerUtilizatori;
    private CredentialeUtilizator user = CredentialeUtilizator.getInstance();
    
    public FereastraLogin(){
        super("Conectare utilizator");
        tUser = new JTextField(20);
        tPassword = new JPasswordField(10);
        lUser = new JLabel("    Username: ");
        lPassword = new JLabel("    Parola: ");
        
        var pInfo = new JPanel(new GridLayout(2,2,10,10));
        pInfo.add(lUser);
        pInfo.add(tUser);
        pInfo.add(lPassword);
        pInfo.add(tPassword);
        this.add(pInfo, BorderLayout.NORTH);
                
        bLogin = new JButton("Autentificare");
        bSignup = new JButton("Inregistrare");
        var pOptions = new JPanel(new FlowLayout(FlowLayout.CENTER));
        pOptions.add(bLogin);
        pOptions.add(bSignup);
        this.add(pOptions, BorderLayout.CENTER);
        
        bLogin.addActionListener(new ButtonListener());
        bSignup.addActionListener(new ButtonListener());
        
        managerUtilizatori = ManagerUtilizatori.getInstance(); 
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        pack();
        setLocationRelativeTo(null);
    }
    private class ButtonListener implements ActionListener{
        @Override
        public void actionPerformed(ActionEvent e){
            String username = tUser.getText();
            String p = new String(tPassword.getPassword());

            if(e.getSource() == bLogin)
                if(managerUtilizatori.getUtilizator(username, p) != null){
                    user.setUser(username, p);
                    FereastraLogin.this.dispose();
                    f = new FereastraMeniu(username);
                    f.setSize(600, 350);//
                    f.setLocationRelativeTo(null);
                    f.setVisible(true);
                    f.setResizable(false);
                    f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                }
                else
                    JOptionPane.showMessageDialog(null, "Conectare eșuată! Date invalide!");

            if(e.getSource() == bSignup)
                if (username.isEmpty() || p.isEmpty())
                    JOptionPane.showMessageDialog(null, "Introduceți un email și o parolă!");
                else
                    if (managerUtilizatori.getUtilizator(username, p) != null)
                        JOptionPane.showMessageDialog(null, "     Cont deja existent!");
                    else
                        {
                           var newUser = managerUtilizatori.inregistreazaUtilizator(username, p);
                           if(newUser != null) {
                                managerUtilizatori.salveaza(newUser);
                                user.setUser(username, p);
                                FereastraLogin.this.dispose();

                               f = new FereastraMesaj();
                               f.setSize(300, 100);
                               f.setLocationRelativeTo(null);
                               f.setResizable(false);
                               f.setVisible(true);
                            }
                        }
        }
    }
}

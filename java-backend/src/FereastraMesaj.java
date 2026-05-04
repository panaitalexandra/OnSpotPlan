//import java.awt.*;
//import javax.swing.*;
//import java.awt.event.*;
///**
// *
// * @author Panait Claudia-Alexandra
// */
//public class FereastraMesaj extends JFrame {
//    private JButton bCompleteaza;
//    private JLabel lMesaj;
//    private CredentialeUtilizator user = CredentialeUtilizator.getInstance();
//
//    public FereastraMesaj() {
//        super("Informare");
//        lMesaj = new JLabel("     Continua prin completarea profilului!");
//        bCompleteaza = new JButton("Completeaza profilul");
//
//        var pContent = new JPanel();
//        pContent.add(lMesaj);
//        this.add(pContent, BorderLayout.CENTER);
//
//        var pButton = new JPanel();
//        pButton.add(bCompleteaza);
//        this.add(pButton, BorderLayout.SOUTH);
//
//        bCompleteaza.addActionListener(e -> {
//                FereastraMesaj.this.dispose();
//                FereastraMeniu fMeniu = new FereastraMeniu(user.getUser());
//                fMeniu.setVisible(false);
//                fMeniu.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//
//            FereastraProfil fProfil = new FereastraProfil(fMeniu);
//                fProfil.setSize(500, 400);
//                fProfil.setLocationRelativeTo(null);
//                fProfil.setResizable(false);
//                fProfil.setVisible(true);
//            });
//    }
//}

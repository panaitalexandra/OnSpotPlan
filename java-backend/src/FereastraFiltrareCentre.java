//import java.awt.*;
//import javax.swing.*;
///**
// *
// * @author Panait Claudia-Alexandra
// */
//public class FereastraFiltrareCentre extends JFrame{
//    private JFrame f;
//    private JComboBox<String> cbJudet;
//    private JButton bFiltreaza, bInapoi;
//    private Client client;
//    private CredentialeUtilizator user = CredentialeUtilizator.getInstance();
//
//    public FereastraFiltrareCentre(Client b){
//        super("Filtrare centre");
//        this.client = b;
//
//        cbJudet = new JComboBox();
//        bFiltreaza = new JButton("Filtrează");
//        bInapoi = new JButton("Înapoi");
//
//        var pCentre = new JPanel(new FlowLayout(FlowLayout.CENTER, 20, 20));
//        pCentre.setPreferredSize(new Dimension(400, 80));
//        pCentre.add(cbJudet);
//        add(pCentre, BorderLayout.CENTER);
//
//        var pButton = new JPanel(new FlowLayout(FlowLayout.CENTER, 20, 20));
//        pButton.setPreferredSize(new Dimension(400, 80));
//        pButton.add(bFiltreaza);
//        pButton.add(bInapoi);
//        add(pButton, BorderLayout.SOUTH);
//
//        bFiltreaza.addActionListener(e -> {
//            String judet = (String) cbJudet.getSelectedItem();
//            FereastraFiltrareCentre.this.dispose();
//            f = new FereastraSelectareCentru(judet, client);
//            f.setVisible(true);
//            f.setSize(500, 200);
//            f.setResizable(false);
//            f.setLocationRelativeTo(null);
//        });
//
//        bInapoi.addActionListener(e -> {
//            FereastraFiltrareCentre.this.dispose();
//            var f = new FereastraMeniu(user.getUser());
//            f.setSize(600, 400);
//            f.setLocationRelativeTo(null);
//            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//            f.setResizable(false);
//            f.setVisible(true);
//        });
//        incarcaJudete();
//    }
//    private void incarcaJudete() {
//        String[] judete = {"Constanta", "Ialomita", "Tulcea", "Calarasi", "Braila", "Ilfov"};
//        for (String judet : judete)
//            cbJudet.addItem(judet);
//    }
//}
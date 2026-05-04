//import javax.swing.*;
//import java.awt.*;
//import java.io.*;
//import javax.swing.table.*;
///**
// *
// * @author Panait Claudia-Alexandra
// */
//public class FereastraSelectareCentru extends JFrame {
//    private JTable tabelCentre;
//    private DefaultTableModel modelTabel;
//    private JButton bInregistreaza, bInapoi;
//    private Client client;
//    private EmailService notificator = new EmailService();
//    private JFrame f;
//    private CredentialeUtilizator user = CredentialeUtilizator.getInstance();
//    private Timer timer;
//
//    public FereastraSelectareCentru(String judet, Client b) {
//        super("Centre vaccinare - " + judet);
//        this.client = b;
//        modelTabel = new DefaultTableModel(new String[]{"Nume Centru"}, 0);
//        tabelCentre = new JTable(modelTabel);
//        JScrollPane scroll = new JScrollPane(tabelCentre);
//        bInregistreaza = new JButton("Înregistrează-te pe lista de așteptare");
//        bInapoi = new JButton("Înapoi");
//        notificator = new EmailService();
//
//        var pUp = new JPanel(new BorderLayout());
//        pUp.add(scroll, BorderLayout.CENTER);
//        add(pUp);
//
//        var pDown = new JPanel(new BorderLayout());
//        pDown.setLayout(new FlowLayout());
//        pDown.add(bInregistreaza);
//        pDown.add(bInapoi);
//        add(pDown, BorderLayout.SOUTH);
//
//        incarcaCentre(judet);
//
//        bInregistreaza.addActionListener(e -> {
//            int index = tabelCentre.getSelectedRow();
//            if (index == -1) {
//                JOptionPane.showMessageDialog(this, "Selectează unul dintre centrele disponibile!");
//                return;
//            }
//            String numeCentru = (String) modelTabel.getValueAt(index, 0);
//            String nume = client.getPersoana().getNume();
//            String prenume = client.getPersoana().getPrenume();
//
//            if (!esteInListaAsteptare(nume, prenume, numeCentru)) {
//                inregistreazaInListaAsteptare(nume, prenume, numeCentru);
//                JOptionPane.showMessageDialog(this, "Te-ai înregistrat pe lista de așteptare la centrul: " + numeCentru);
//                this.dispose();
//                f = new FereastraMeniu(user.getUser());
//                f.setSize(600, 400);//
//                f.setLocationRelativeTo(null);
//                f.setVisible(true);
//                f.setResizable(false);
//                f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//
//                timer = new Timer(400, x -> {
//                    notificator.adaugaNotificare(client.getPersoana().getCNP(), numeCentru);
//                    timer.stop();
//                });
//                timer.start();
//            }
//            else
//                {
//                    int opt = JOptionPane.showConfirmDialog(this,
//                            "Ești deja înregistrat pe lista de așteptare la acest centru.\n" +
//                                    "Dorești să confirmi programarea?",
//                            "Confirmare programare",
//                            JOptionPane.YES_NO_OPTION);
//
//                    if (opt == JOptionPane.YES_OPTION) {
//                        FereastraProgramare fProg = new FereastraProgramare(b, numeCentru);
//                        fProg.setSize(600, 400);
//                        fProg.setLocationRelativeTo(null);
//                        fProg.setResizable(false);
//                        fProg.setVisible(true);
//                        this.dispose();
//                    }
//                }
//        });
//
//        bInapoi.addActionListener(e -> {
//            FereastraSelectareCentru.this.dispose();
//            var f = new FereastraFiltrareCentre(client);
//            f.setSize(300, 180);
//            f.setLocationRelativeTo(null);
//            f.setVisible(true);
//            f.setResizable(false);
//            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//        });
//    }
//    private void incarcaCentre(String judet) {
//        String numeFisier = "centre" + judet + ".txt";
//        File fisierLocalitati = new File(numeFisier);
//
//        try (BufferedReader br = new BufferedReader(new FileReader(fisierLocalitati))) {
//            String linie;
//            while ((linie = br.readLine()) != null) {
//                String numeCentru = linie.trim();
//                modelTabel.addRow(new Object[]{numeCentru});
//            }
//        } catch (IOException ex) {
//            ex.printStackTrace();
//            JOptionPane.showMessageDialog(this, "Eroare");
//        }
//    }
//    private boolean esteInListaAsteptare (String nume, String prenume, String centru){
//        File f = new File("listaAsteptare.txt");
//        if (!f.exists()) return false;
//
//        try (BufferedReader br = new BufferedReader(new FileReader(f))) {
//            String linie;
//            while ((linie = br.readLine()) != null) {
//                String[] parti = linie.split(";");
//                if (parti.length == 3)
//                    if (parti[0].equals(nume) && parti[1].equals(prenume) && parti[2].equals(centru))
//                        return true;
//            }
//        } catch (IOException e) { e.printStackTrace(); }
//        return false;
//    }
//
//    private void inregistreazaInListaAsteptare (String nume, String prenume, String centru){
//        try (FileWriter fw = new FileWriter("listaAsteptare.txt", true);
//             BufferedWriter bw = new BufferedWriter(fw)) {
//            bw.write(nume + ";" + prenume + ";" + centru);
//            bw.newLine();
//        } catch (IOException e) { e.printStackTrace(); }
//    }
//}
//
//

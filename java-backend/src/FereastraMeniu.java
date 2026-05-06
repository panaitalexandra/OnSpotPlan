///**
// *
// * @author Panait Claudia-Alexandra
// */
//import java.awt.*;
//import java.awt.event.*;
//import java.io.BufferedReader;
//import java.io.File;
//import java.io.FileReader;
//import java.io.IOException;
//import javax.swing.*;
//import javax.swing.table.*;
//import java.util.List;
//
//
//public class FereastraMeniu extends JFrame {
//    private JFrame f;
//    private JLabel lNume, lPrenume, lCnp, lSerie, lNumar, lJudet, lLocalitate, lVarsta, lRisc, lDizabilitati;// fereastra interna nedeclarata Detalii - bVizualizeaza
//    private JButton bVizualizeaza, bProgrameaza, bStergeProgramare, bAdaugaProfil;
//    private JTable tabelBeneficiari;
//    private DefaultTableModel modelTabel;
//    private ManagerClienti managerClienti;
//    private ManagerProgramari managerProgramari;
//    private ManagerListaAsteptare managerListaAsteptare;
//    private String emailUtilizator;
//
//    public FereastraMeniu(String emailUtilizator) {
//        super("Aplicație Vaccinare");
//        this.emailUtilizator = emailUtilizator;
//        managerClienti = ManagerClienti.getInstance(emailUtilizator);
//        managerProgramari = new ManagerProgramari();
//        managerListaAsteptare = ManagerListaAsteptare.getInstance();
//        managerListaAsteptare.incarcaDinFisier("listaAsteptare.txt");
//
//        modelTabel = new DefaultTableModel(new String[]{"Nume", "Prenume", "CNP"}, 0);//initial 3 linii, 0 coloane
//        tabelBeneficiari = new JTable(modelTabel);
//        JScrollPane scrollPane = new JScrollPane(tabelBeneficiari);
//        scrollPane.setPreferredSize(new Dimension(350, 300));
//
//        for (Client b : managerClienti.getLista())
//            modelTabel.addRow(new Object[]{b.getPersoana().getNume(), b.getPersoana().getPrenume(), b.getPersoana().getCNP() } );
//
//        JPanel pList = new JPanel(new BorderLayout());
//        pList.add(new JLabel("Listă Beneficiari"), BorderLayout.NORTH);
//        pList.add(scrollPane, BorderLayout.CENTER);
//
//        JPanel pOptions = new JPanel(new GridLayout(4,1,0,30));
//        bAdaugaProfil = new JButton("Adaugă Profil");
//        bVizualizeaza = new JButton("Vizualizează");
//        bProgrameaza = new JButton("Programează");
//        bStergeProgramare = new JButton("Șterge programarea");
//
//        pOptions.add(bVizualizeaza);
//        pOptions.add(bProgrameaza);
//        pOptions.add(bStergeProgramare);
//        pOptions.add(bAdaugaProfil);
//
//        getContentPane().setLayout(new FlowLayout(FlowLayout.LEFT, 30, 30));//prelucrare directa a containerului interior panoului
//        add(pList);
//        add(pOptions);
//
//        bVizualizeaza.addActionListener(new ButtonListener());
//        bProgrameaza.addActionListener(new ButtonListener());
//        bStergeProgramare.addActionListener(new ButtonListener());
//
//        bAdaugaProfil.addActionListener(e -> {
//            if(managerClienti.poateAdaugaBeneficiar()) {
//                FereastraProfil fProfil = new FereastraProfil(FereastraMeniu.this);
//                fProfil.setSize(600, 400);
//                fProfil.setLocationRelativeTo(null);
//                fProfil.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
//                fProfil.setVisible(true);
//            }
//            else
//                JOptionPane.showMessageDialog(null, "Ați atins limita de 10 beneficiari înregistrați.");
//
//        });
//
//    }
//     private class ButtonListener implements ActionListener {
//        private int index;//va deveni randul selectat din interiorul tabelului
//        @Override
//        public void actionPerformed(ActionEvent e) {
//            if(e.getSource() == bVizualizeaza)
//            {
//                index = tabelBeneficiari.getSelectedRow();
//                if (index == -1) {
//                    JOptionPane.showMessageDialog(FereastraMeniu.this, "Selectează un beneficiar din tabel");
//                    return;
//                }
//
//                Client b = managerClienti.getLista().get(index);
//                IdentityCard act = b.getPersoana().getCarteIdentitate();
//
//                String serie = (act != null && act.getSerie() != null) ? act.getSerie() : "necunoscută";
//                String numar = (act != null && act.getNumber() != null) ? act.getNumber() : "necunoscut";
//                String judet = (act != null && act.getJudet() != null) ? act.getJudet() : "necunoscut";
//                String localitate = (act != null && act.getCity() != null) ? act.getCity() : "necunoscut";
//
//                JDialog FereastraDetalii = new JDialog(FereastraMeniu.this, "Detalii beneficiar", true);
//                JPanel pInfo = new JPanel(new GridLayout(0, 1, 10, 10));
//
//                lNume = new JLabel("   Nume: " + b.getPersoana().getNume());
//                lPrenume = new JLabel("   Prenume: " + b.getPersoana().getPrenume());
//                lCnp = new JLabel("   CNP: " + b.getPersoana().getCNP());
//                lSerie = new JLabel("   Serie: " + serie);
//                lNumar = new JLabel("   Număr: " + numar);
//                lJudet = new JLabel("   Județ: " + judet);
//                lLocalitate = new JLabel("   Localitate: " + localitate);
//                lVarsta = new JLabel("   Vârstă: " + b.getVarsta());
//                //lDizabilitati = new JLabel( "   " + b.estePersoanaCuDizabilitati());
//
//                pInfo.add(lNume);
//                pInfo.add(lPrenume);
//                pInfo.add(lCnp);
//                pInfo.add(lSerie);
//                pInfo.add(lNumar);
//                pInfo.add(lJudet);
//                pInfo.add(lLocalitate);
//                pInfo.add(lVarsta);
//                pInfo.add(lRisc);
//                pInfo.add(lDizabilitati);
//                FereastraDetalii.add(pInfo);
//
//                JPanel pButton = new JPanel(new FlowLayout(FlowLayout.CENTER));
//                JButton bInapoi = new JButton("Inapoi");
//                pButton.add(bInapoi);
//                FereastraDetalii.add(pButton, BorderLayout.SOUTH);
//
//                bInapoi.addActionListener(e2 -> FereastraDetalii.dispose());
//
//                FereastraDetalii.setSize(400, 450);
//                FereastraDetalii.setLocationRelativeTo(null);
//                FereastraDetalii.setResizable(false);
//                FereastraDetalii.setVisible(true);
//            }
//            else
//                if(e.getSource() == bProgrameaza)
//                {
//                    index = tabelBeneficiari.getSelectedRow();
//                    if (index == -1) {
//                        JOptionPane.showMessageDialog(FereastraMeniu.this, "Selectează un beneficiar pentru programare.");
//                        return;
//                    }
//                    Client b = managerClienti.getLista().get(index);
//                    FereastraMeniu.this.setVisible(false);
//
//                    boolean continuaInMeniu = false;
//                    if(esteInProgramari(b)) {
//                        FereastraMeniu.this.setVisible(true);
//                        JOptionPane.showMessageDialog(FereastraMeniu.this, "Beneficiarul are deja o programare înregistrată.");
//                        continuaInMeniu = true;
//                    }
//                    if (esteInListaAsteptare(b)) {
//                            String centru = centruDinLista(b);
//                            FereastraProgramare fProg = new FereastraProgramare(b, centru);
//
//                            fProg.setSize(600, 400);
//                            fProg.setLocationRelativeTo(null);
//                            fProg.setVisible(true);
//                            String cnp = b.getPersoana().getCNP();
//                            managerListaAsteptare.stergeBeneficiar(centru, cnp);
//                            managerListaAsteptare.salveazaInFisier("listaAsteptare.txt");
//
//                    }
//                    else {
//                        if (!continuaInMeniu) {
//                            f = new FereastraFiltrareCentre(b);
//                            f.setSize(300, 180);
//                            f.setLocationRelativeTo(null);
//                            f.setVisible(true);
//                            f.setResizable(false);
//                            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//                        } else
//                            FereastraMeniu.this.setVisible(true);
//                    }
//                }
//                else
//                {
//                    index = tabelBeneficiari.getSelectedRow();
//                    if (index == -1) {
//                        JOptionPane.showMessageDialog(FereastraMeniu.this, "Selectează un beneficiar pentru a sterge programarea!");
//                        return;
//                    }
//
//                    Client b = managerClienti.getLista().get(index);
//                    List<Programare> programari = managerProgramari.getProgramariPentruBeneficiar(b);
//
//                    if (programari == null || programari.isEmpty()) {
//                        JOptionPane.showMessageDialog(FereastraMeniu.this, "Beneficiarul nu are nicio programare înregistrată.");
//                        return;
//                    }
//                    Programare p = programari.get(0);
//                    String centru = p.getCentruVaccinare();
//                    String data = p.getData().toString();
//                    String ora = p.getOra().toString();
//
//                    String mesaj = "Ești sigur că vrei să anulezi programarea pentru Beneficiarul "
//                            + b.getPersoana().getNume() + " " + b.getPersoana().getPrenume() + "\n"
//                            + " de la " + centru
//                            + " din intervalul " + data + " Ora " + ora
//                            + "?\nAtenție! Se vor anula inclusiv programările pentru rapeluri!";
//
//                    String[] optiuni = {"Confirmă", "Renunță"}; // Butoane personalizate
//
//                    int confirm = JOptionPane.showOptionDialog(
//                            FereastraMeniu.this,
//                            mesaj,
//                            "Confirmare anulare",
//                            JOptionPane.YES_NO_OPTION,
//                            JOptionPane.QUESTION_MESSAGE,
//                            null,
//                            optiuni,
//                            optiuni[1]
//                    );
//
//                    if (confirm == JOptionPane.YES_OPTION) {
//                        boolean sters = managerProgramari.stergeProgramare(b);
//                        if (sters) {
//                            String cnp = b.getPersoana().getCNP();
//                            centru = null;
//
//                            for (String c : managerListaAsteptare.getCentre())
//                                if (managerListaAsteptare.esteInLista(c, cnp)) {
//                                    centru = c;
//                                    break;
//                                }
//
//                            if (centru != null) {
//                                managerListaAsteptare.stergeBeneficiar(centru, cnp);
//                                managerListaAsteptare.salveazaInFisier("listaAsteptare.txt");
//                                System.out.println("Beneficiarul a fost eliminat din lista de așteptare pentru centrul: " + centru);
//                            }
//                            JOptionPane.showMessageDialog(FereastraMeniu.this, "Programarea a fost ștearsă cu succes.");
//                        }
//                        else
//                            JOptionPane.showMessageDialog(FereastraMeniu.this, "Eroare la ștergerea programării.");
//                    }
//                }
//        }
//    }
//
//    public void adaugaBeneficiarInTabel(Client b) {
//        if (managerClienti.adaugaBeneficiar(b)) {
//            modelTabel.addRow(new Object[]{ b.getPersoana().getNume(), b.getPersoana().getPrenume(), b.getPersoana().getCNP() });
//            managerClienti.salveaza();
//        }
//    }
//
//    private boolean esteInProgramari(Client b){
//        File f = new File("programari.txt");
//        if (!f.exists()) return false;
//
//        String cnp = b.getPersoana().getCNP();
//        try (BufferedReader br = new BufferedReader(new FileReader(f))) {
//            String linie;
//            while ((linie = br.readLine()) != null) {
//                String[] parti = linie.split(";");
//                if (parti.length >= 3) {
//                    String cnpDinFisier = parti[2].trim();
//                    if (cnp.equals(cnpDinFisier))
//                        return true;
//                }
//            }
//        } catch (IOException e) { e.printStackTrace(); }
//        return false;
//
//    }
//    private boolean esteInListaAsteptare(Client b) {
//        File f = new File("listaAsteptare.txt");
//        if (!f.exists()) return false;
//
//        String nume = b.getPersoana().getNume().trim();
//        try (BufferedReader br = new BufferedReader(new FileReader(f))) {
//            String linie;
//            while ((linie = br.readLine()) != null) {
//                String[] parti = linie.split(";");
//                if (parti.length >= 1) {
//                    String numeDinFisier = parti[0].trim();
//                    if (nume.equals(numeDinFisier))
//                        return true;
//                }
//            }
//        } catch (IOException e) { e.printStackTrace(); }
//        return false;
//    }
//    private String centruDinLista(Client b) {
//        File f = new File("listaAsteptare.txt");
//        if (!f.exists()) return null;
//
//        String nume = b.getPersoana().getNume();
//        String prenume = b.getPersoana().getPrenume();
//
//        try (BufferedReader br = new BufferedReader(new FileReader(f))) {
//            String linie;
//            while ((linie = br.readLine()) != null) {
//                String[] parti = linie.split(";");
//                if (parti.length == 3)
//                    if (parti[0].equals(nume) && parti[1].equals(prenume))
//                        return parti[2]; // centrul
//            }
//        } catch (IOException e) { e.printStackTrace(); }
//        return null;
//    }
//}
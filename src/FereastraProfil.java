import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.io.*;
/**
 *
 * @author Panait Claudia-Alexandra
 */
public class FereastraProfil extends JFrame {
    private JLabel lNume, lPrenume, lCnp, lSerie, lNumar, lOption, lJudet, lLocalitate;
    private JTextField tNume, tPrenume, tCnp, tSerie, tNumar;
    private JButton bFinal;
    private JCheckBox cbOption;
    private JComboBox<String> cbJudet, cbLocalitate;
    private FereastraMeniu f;
    private Beneficiar b;

    public FereastraProfil(FereastraMeniu f) {//constructorul primeste paramatrul pentru a se realiza comunicarea intre cele doua ferestre
        super("Completare profil");      
        this.f = f;        
        lNume = new JLabel("   Nume: ");
        lPrenume = new JLabel("   Prenume: ");
        lCnp = new JLabel("   CNP: ");        
        lSerie = new JLabel("   Serie: ");    
        lNumar = new JLabel("   Număr: ");
        lJudet = new JLabel("   Județ: ");
        lLocalitate = new JLabel("   Localitate: ");    
        
        cbJudet = new JComboBox();    
        cbLocalitate = new JComboBox();
        lOption = new JLabel("Sunt persoană cu dizabilități");
        
        tNume = new JTextField(30);
        tPrenume = new JTextField(10);
        tCnp = new JTextField(10);
        tSerie = new JTextField(10);
        tNumar = new JTextField(10);
        
        cbOption = new JCheckBox();
        
        var pInfo = new JPanel(new GridLayout(8,2,10,10));
        pInfo.add(lNume);       pInfo.add(tNume);
        pInfo.add(lPrenume);    pInfo.add(tPrenume);
        pInfo.add(lCnp);        pInfo.add(tCnp);
        pInfo.add(lSerie);      pInfo.add(tSerie);
        pInfo.add(lNumar);      pInfo.add(tNumar);
        pInfo.add(lJudet);      pInfo.add(cbJudet);        
        pInfo.add(lLocalitate); pInfo.add(cbLocalitate);
        this.add(pInfo, BorderLayout.NORTH);
        
        var pOption = new JPanel(new FlowLayout(FlowLayout.LEFT));
        pOption.add(cbOption);
        pOption.add(lOption);
        this.add(pOption);
                
        bFinal = new JButton("Completează Profil");
        var pOptions = new JPanel(new FlowLayout(FlowLayout.CENTER));
        pOptions.add(bFinal);
        this.add(pOptions, BorderLayout.SOUTH);
        
        bFinal.addActionListener(new ButtonListener());
        
        incarcaJudete();
    }
    private void incarcaJudete() {
        String[] judete = {"Constanta", "Ialomita", "Tulcea", "Calarasi", "Braila", "Ilfov"};//hardcoded 
        for (String judet : judete) 
            cbJudet.addItem(judet);
        
        cbJudet.addActionListener(e -> {
            String judetSelectat = (String) cbJudet.getSelectedItem();
            incarcaLocalitati(judetSelectat);
        });
    }
    private void incarcaLocalitati(String judet) {
        cbLocalitate.removeAllItems();//curatare explicita
        String numeFisier = "jud" + judet + ".txt";
        File fisierLocalitati = new File(numeFisier);
    
        try (BufferedReader br = new BufferedReader(new FileReader(fisierLocalitati))) {
            String linie;
            while ((linie = br.readLine()) != null) 
                cbLocalitate.addItem(linie);
            cbLocalitate.setEnabled(true);
        } catch (IOException ex) {
            ex.printStackTrace();
            cbLocalitate.setEnabled(false);//prindem eroarea in cazul fisierului lipsa
        }
    }

    private class ButtonListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            String nume = tNume.getText();
            String prenume = tPrenume.getText();
            String cnp = tCnp.getText();
            String serie = tSerie.getText();
            String numar = tNumar.getText();
            String judet = (String) cbJudet.getSelectedItem();
            String localitate = (String) cbLocalitate.getSelectedItem();
            
            if (nume.isEmpty() || prenume.isEmpty() || cnp.isEmpty() || serie.isEmpty() || numar.isEmpty() || judet.isEmpty() || localitate.isEmpty()) {
                JOptionPane.showMessageDialog(null, "Completați toate câmpurile pentru a putea continua!");
                return;
            }
            
            if (cnp.length() < 13) {
                JOptionPane.showMessageDialog(null, "CNP-ul trebuie să conțină 13 caractere!");
                return;
            }

            String dizabilitati = cbOption.isSelected() ? "Persoană cu dizabilități" : "Persoană fără dizabilități";
            b = new Beneficiar(nume, prenume, cnp, serie, numar, judet, localitate, dizabilitati);

            if (b.calculeazaVarsta(cnp) >= 17) {
                f.adaugaBeneficiarInTabel(b);
                JOptionPane.showMessageDialog(null, "Profil completat! Ați fost adaugat în lista de beneficiari.");

                FereastraProfil.this.dispose();
                f.setSize(600, 400);
                f.setLocationRelativeTo(null);
                f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                f.setResizable(false);
                f.setVisible(true);
            } else {
                JOptionPane.showMessageDialog(null, "Doar persoanele de peste 16 ani pot să-și înregistreze o programare la vaccinarea anti-COVID19.");
                return;
            }

        }
    }
}
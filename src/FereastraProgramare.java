/**
 *
 * @author Mihaila Alexia-Andreea
 */
import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.io.*;
import java.time.format.TextStyle;
import java.awt.*;
import java.time.*;
import java.util.*;

public class FereastraProgramare extends JFrame{
    private JLabel lblLunaAn;
    private JTable tabelProgramari;
    private DefaultTableModel modelTabel;
    private JComboBox<String> cbOre;
    private JButton bConfirma, bInapoi;
    private String centruVaccinare;
    private Locale localeRO = new Locale("ro", "RO");
    private Map<LocalDate, Integer> locuriDisponibilePeZile = new LinkedHashMap<>();
    private JFrame f;
    private Client client;
    private CredentialeUtilizator user = CredentialeUtilizator.getInstance();
    private EmailService EmailService;

    public FereastraProgramare(Client client, String centru) {
        this(client, centru, YearMonth.now().plusMonths(1));
    }

    public FereastraProgramare(Client client, String centru, YearMonth lunaDisponibila) {
        super("Programare vaccinare - " + centru);
        this.centruVaccinare = centru;
        this.client = client;

        incarcaLocuriDisponibileDinFisier(lunaDisponibila);
        locuriDisponibilePeZile = genereazaLocuriDisponibile(lunaDisponibila);
        setLayout(new BorderLayout(10, 10));

        lblLunaAn = new JLabel(lunaDisponibila.getMonth().getDisplayName(TextStyle.FULL, localeRO) + " " + lunaDisponibila.getYear());
        lblLunaAn.setFont(new Font("Arial", Font.BOLD, 18));
        lblLunaAn.setHorizontalAlignment(SwingConstants.CENTER);
        add(lblLunaAn, BorderLayout.NORTH);

        modelTabel = new DefaultTableModel(new String[]{"Ziua", "Data", "Locuri disponibile"}, 0) {
            @Override
            public boolean isCellEditable(int row, int column) {
                return false;
            }
        };
        tabelProgramari = new JTable(modelTabel);
        tabelProgramari.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);

        incarcaTabelCuZile(lunaDisponibila);

        add(new JScrollPane(tabelProgramari), BorderLayout.CENTER);

        cbOre = new JComboBox<>(new String[]{"08:00", "09:00", "10:00", "11:00", "14:00", "15:00", "16:00"});
        JPanel pOre = new JPanel(new FlowLayout(FlowLayout.CENTER));
        pOre.add(new JLabel("Selectează ora:"));
        pOre.add(cbOre);

        bConfirma = new JButton("Confirmă programarea");
        bInapoi = new JButton("Înapoi");

        JPanel pJos = new JPanel(new FlowLayout(FlowLayout.CENTER, 20, 10));
        pJos.add(pOre);
        pJos.add(bConfirma);
        pJos.add(bInapoi);

        add(pJos, BorderLayout.SOUTH);

        EmailService = new EmailService();

        bConfirma.addActionListener(e -> {
            confirmaProgramarea();

        });

        bInapoi.addActionListener(e -> {
            this.dispose();
            f = new FereastraMeniu(user.getUser());
            f.setSize(600, 400);//
            f.setLocationRelativeTo(null);
            f.setVisible(true);
            f.setResizable(false);
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        });

        setSize(500, 400);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
    }

    private Map<LocalDate, Integer> genereazaLocuriDisponibile(YearMonth luna) {
        Map<LocalDate, Integer> locuri = new LinkedHashMap<>();
        for (int zi = 1; zi <= luna.lengthOfMonth(); zi++) {
            int disponibile = (int)(Math.random() * 6);
            locuri.put(luna.atDay(zi), disponibile);
        }
        return locuri;
    }
    private void salveazaLocuriDisponibile() {
        File f = new File("locuriDisponibile_" + centruVaccinare + ".txt");
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(f))) {
            for (Map.Entry<LocalDate, Integer> entry : locuriDisponibilePeZile.entrySet()) {
                bw.write(entry.getKey().toString() + ";" + entry.getValue());
                bw.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void incarcaLocuriDisponibileDinFisier(YearMonth luna) {
        locuriDisponibilePeZile.clear();
        File f = new File("locuriDisponibile_" + centruVaccinare + ".txt");
        if (!f.exists()) {
            locuriDisponibilePeZile = genereazaLocuriDisponibile(luna);
            salveazaLocuriDisponibile();
            return;
        }
        try (BufferedReader br = new BufferedReader(new FileReader(f))) {
            String linie;
            while ((linie = br.readLine()) != null) {
                String[] parti = linie.split(";");
                if (parti.length == 2) {
                    LocalDate data = LocalDate.parse(parti[0]);
                    int nrLocuri = Integer.parseInt(parti[1]);
                    locuriDisponibilePeZile.put(data, nrLocuri);
                }
            }
        } catch (IOException e) { e.printStackTrace(); }
    }
    private void incarcaTabelCuZile(YearMonth luna) {
        modelTabel.setRowCount(0);
        for (LocalDate data : locuriDisponibilePeZile.keySet()) {
            DayOfWeek ziSapt = data.getDayOfWeek();
            String ziNume = ziSapt.getDisplayName(TextStyle.FULL, localeRO);
            int locuri = locuriDisponibilePeZile.get(data);
            modelTabel.addRow(new Object[]{ziNume, data.getDayOfMonth(), locuri});
        }
    }

    private void confirmaProgramarea() {
        int randSelectat = tabelProgramari.getSelectedRow();
        if (randSelectat == -1) {
            JOptionPane.showMessageDialog(this, "Selectați o zi pentru programare!", "Eroare", JOptionPane.ERROR_MESSAGE);
            return;
        }

        int locuri = (int) modelTabel.getValueAt(randSelectat, 2);
        if (locuri == 0) {
            JOptionPane.showMessageDialog(this, "Nu mai sunt locuri disponibile în ziua selectată.", "Eroare", JOptionPane.ERROR_MESSAGE);
            return;
        }

        int zi = (int) modelTabel.getValueAt(randSelectat, 1);
        YearMonth luna = YearMonth.of(LocalDate.now().getYear(), LocalDate.now().getMonth());

        LocalDate dataSelectata = null;
        for (LocalDate d : locuriDisponibilePeZile.keySet()) {
            if (d.getDayOfMonth() == zi) {
                dataSelectata = d;
                break;
            }
        }

        String ora = (String) cbOre.getSelectedItem();
        String oraSelectata = (String) cbOre.getSelectedItem();
        LocalTime oraS = LocalTime.parse(oraSelectata);

        Vaccin vaccin = Vaccin.alegeVaccin();
        LocalDate dataRapel = dataSelectata.plusDays(vaccin.getZilePanaLaRapel());
        Programare p = new Programare(client, centruVaccinare, dataSelectata, oraS, vaccin);

        ManagerProgramari manager = new ManagerProgramari();
        boolean adaugat = manager.adaugaProgramare(p);
        if (!adaugat) {
            JOptionPane.showMessageDialog(this, "Programarea există deja!", "Eroare", JOptionPane.ERROR_MESSAGE);
            return;
        }
        locuriDisponibilePeZile.put(dataSelectata, locuri - 1);
        salveazaLocuriDisponibile();
        incarcaTabelCuZile(YearMonth.from(dataSelectata));

        String mesaj = "Destinatar: " + user.getUser() + "\nConfirmare programare pentru beneficiarul înregistrat în sistem\n" +
                "Nume: " + client.getPersoana().getNume() + " " + client.getPersoana().getPrenume() + "\n" +
                "Centru vaccinare: " + centruVaccinare + "\n" +
                "Data: " + dataSelectata + " (" + dataSelectata.getDayOfWeek().getDisplayName(TextStyle.FULL, localeRO) + ")\n" +
                "Ora: " + ora + "\n" +
                "Vaccin: " + vaccin.getNume() + "\n" +
                "Rapel: " + dataRapel + " (" + dataRapel.getDayOfWeek().getDisplayName(TextStyle.FULL, localeRO) + ")\n\n" +
                "Vă mulțumim pentru programare!";

        JOptionPane.showMessageDialog(this, mesaj, "Email confirmare programare", JOptionPane.INFORMATION_MESSAGE);
        EmailService.scrieMail(user.getUser());

        this.dispose();
        f = new FereastraMeniu(user.getUser());
        f.setSize(600, 400);//
        f.setLocationRelativeTo(null);
        f.setVisible(true);
        f.setResizable(false);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}


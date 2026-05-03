import javax.swing.*;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
/**
 *
 * @author Mihaila Alexia-Andreea
 */
public class EmailService {
    private final String fisierNotificari = "notificari.txt";

    public void adaugaNotificare(String email, String centru) {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(fisierNotificari, true))) {
            bw.write(email + ";" + centru);
            bw.newLine();

            JOptionPane.showMessageDialog(null,
                    "Vă informăm că au apărut locuri disponibile pentru programarea la vaccinare la " + centru + "\n" +
                            "Vă invităm să accesați aplicația noastră pentru a continua procesul de programare, selectând intervalul orar dorit.\n" +
                            "Mulțumim pentru implicarea dumneavoastră în procesul de vaccinare!",
                    "Notificare programare",
                    javax.swing.JOptionPane.INFORMATION_MESSAGE);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public void scrieMail(String email) {
        File fisier = new File("emailProgramari.txt");
        boolean exista = fisier.exists();

        try (FileWriter writer = new FileWriter(fisier, true)) {
            if (!exista)
                writer.write("Lista emailuri cu programarea confirmata\n");
            writer.write(email + "\n");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
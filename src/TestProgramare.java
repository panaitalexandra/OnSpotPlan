import javax.swing.JFrame;
/**
 *
 * @author Panait Claudia-Alexandra
 */
public class TestProgramare {
    public static void main(String... args){
        var f = new FereastraLogin();
        f.setSize(300, 130);
        f.setLocationRelativeTo(null);
        f.setVisible(true);
        f.setResizable(false);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}

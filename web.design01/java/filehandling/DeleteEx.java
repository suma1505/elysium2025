import java.io.*;
public class DeleteEx {
    public static void main(String[] args) {
        try {
            File f = new File("text.txt");
            f.delete();
            System.out.println("deleted success");
        } catch (Exception e) {
            System.out.println("error");
            e.printStackTrace();           
        }
    }
}

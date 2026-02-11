import java.io.*;
public class Create{
    public static void main(String[] args) {
        try {
            File f = new File("sample.txt");
            f.createNewFile();
            System.out.println("file created");
        } catch (Exception e) {
            System.out.println("error");
        }
    }
}
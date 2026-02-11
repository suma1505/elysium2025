import java.io.*;
import java.util.*;
public class ReadScan {
    public static void main(String[] args) {
        try {
            File f = new File("sample.txt");
            Scanner sc = new Scanner(f);
           while (sc.hasNextLine()) {
                  String line=sc.nextLine();
                  System.out.println(line);
           }
            sc.close();
            
        } catch (Exception e) {
            System.out.println("error");
            e.printStackTrace();
        }
    }  
}

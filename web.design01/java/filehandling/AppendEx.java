import java.io.*;
public class AppendEx {
    public static void main(String[] args) {
        try {
            BufferedWriter bw = new BufferedWriter(new FileWriter("sample.txt",true));
            bw.write("this is append mode");
            bw.close();
            System.out.println("written success");
        } catch (Exception e) {
           
        }
    }
    
}

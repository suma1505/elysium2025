import java.io.*;
public class WriteEx {

    public static void main(String[] args) {
        try {
            BufferedWriter bw = new BufferedWriter(new FileWriter("sample.txt"));
            bw.write("this is java filehandling");
            bw.close();
            System.out.println("written success");
        } catch (Exception e) {
            System.out.println("error");   
            e.printStackTrace();    
        }
    }
}
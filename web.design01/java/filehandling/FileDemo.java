package filehandling;

import java.io.*;

public class FileDemo {
    public static void main(String[] args) throws Exception {
        File f = new File("Demo.txt");

        if (f.createNewFile()) {
            System.out.println("File Created");
        }
        FileWriter fw = new FileWriter(f);
        fw.write("Java File Handling");
        fw.close();

        BufferedReader br = new BufferedReader(new FileReader(f));
        System.out.println(br.readLine());
        br.close();
    }
}

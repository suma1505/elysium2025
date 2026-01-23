package filehandling;

import java.io.*;

public class ReadFile {
    public static void main(String[] args) throws Exception {
        File file=new File("Student.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));
        String line;
        while ((line = br.readLine()) !=null) {
            String[] data = line.split(",");
            System.out.println("ID: " + data[0] + " Name: " + data[1] + " Age: " + data[2]);
        } 
        br.close();    
    }
}

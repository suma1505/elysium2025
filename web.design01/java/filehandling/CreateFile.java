package filehandling;

import java.io.FileWriter;
import java.io.IOException;

public class CreateFile {
    public static void main(String[] args) throws IOException {
        FileWriter fw = new FileWriter("Student.txt",true);
        fw.write("1, uma, 21");
        fw.write("2, prarthana, 21");
        fw.close();

        System.out.println("Data Written Successfully");
    }
}

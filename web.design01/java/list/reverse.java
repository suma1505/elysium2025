package list;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class reverse {
    public static void main(String[] args) {
        List <String> l = new ArrayList<>(Arrays.asList("A","B","C"));
        Collections.reverse(l);
        System.out.println("Reversed string:" + l);
    }
}

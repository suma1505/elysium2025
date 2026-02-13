package list;

import java.util.*;


public class duplicate {
    public static void main(String[] args) {
        List <String> fruits = new ArrayList<>(Arrays.asList("apple","mango","orange","apple","mango"));
        Set <String> fruit = new LinkedHashSet<>(fruits);
        System.out.println("fruit:" + fruit);
    }
}

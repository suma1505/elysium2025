package set;

import java.util.*;

public class string {
    public static void main(String[] args) {
        Set<String> names = new TreeSet<>();
        names.add("Ragavi");
        names.add("Anu");
        names.add("Zara");
        names.add("Kemi");
        names.add("Banu");

        System.out.println("Names (sorted): " + names);

        names.remove("Anu");
        System.out.println("After removing Anu: " + names);

        System.out.println("Does set contain 'Zara'? " + names.contains("Zara"));
    }
}

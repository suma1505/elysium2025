package set;

import java.util.*;

public class reverse {
    public static void main(String[] args) {
        Set<String> reverseSet = new TreeSet<>(Collections.reverseOrder());
        reverseSet.add("Apple");
        reverseSet.add("Banana");
        reverseSet.add("Mango");
        reverseSet.add("Peach");
        System.out.println("Names in reverse order: " + reverseSet);
    }
}

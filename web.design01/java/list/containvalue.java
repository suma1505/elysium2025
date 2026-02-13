package list;

import java.util.*;

public class containvalue {
    public static void main(String[] args) {
        List<String> fruits = new ArrayList<>(Arrays.asList("mango", "banana", "apple"));
        String search = "apple";
        if (fruits.contains(search)) {
            System.out.println(search + " is in the list.");
        } else {
            System.out.println(search + " is NOT in the list.");
        }

    }
}

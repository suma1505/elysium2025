package list;

import java.util.*;

public class sortlist {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>(Arrays.asList("delta", "alpha", "gama","beta","teta"));
        Collections.sort(list);
        System.out.println("Sorted List: " + list);

    }
}

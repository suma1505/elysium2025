package list;

import java.util.*;

public class mergelist {
    public static void main(String[] args) {
        List <Integer> list1 = new ArrayList<>(Arrays.asList(123));
        List <Integer> list2 = new ArrayList<>(Arrays.asList(456));
        list1.addAll(list2);
        System.out.println("merged list:" +list1);

    }
}

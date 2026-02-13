package list;

import java.util.*;

public class maxinlist {
    public static void main(String[] args) {
        List <Integer> list = new ArrayList<>(Arrays.asList(10,5,21,8));
        int max = Collections.max(list);
        System.out.println("maximum number:" + max);
    }
}

package set;

import java.util.*;

public class treeset {
    public static void main(String[] args) {
        Set<Integer> num = new TreeSet<>();
        num.add(30);
        num.add(40);
        num.add(10);
        num.add(20);
        num.add(50);
        System.out.println("sort set:" + num);
        num.remove(30);
        System.out.println("after removing:" +  num);
    }
}

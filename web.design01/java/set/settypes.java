package set;

import java.util.*;

public class settypes {
    public static void main(String[] args) {
        TreeSet<Integer> numbers = new TreeSet<>();
        numbers.addAll(Arrays.asList(10, 20, 30, 40, 50, 60));

        System.out.println("Original: " + numbers);
        System.out.println("Subset (20 to 50): " + numbers.subSet(20, true, 50, true));
        System.out.println("TailSet (>=30): " + numbers.tailSet(30));
        System.out.println("HeadSet (<40): " + numbers.headSet(40));

    }
}

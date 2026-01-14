package mathandWrapper;

import java.util.ArrayList;

public class list {
        public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(10);  // Auto-boxing
        list.add(20);
        list.add(30);
        for (int num : list) {
            System.out.println("Value: " + num); // Auto-unboxing
        }
    }
}

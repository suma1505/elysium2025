package list;

import java.util.*;

public class queue {
    public static void main(String[] args) {
        List<String> q = new LinkedList<>();

        q.add("A");
        q.add("B");
        q.add("C");
        System.out.println("Queue: " + q);

        String removed = q.removeFirst();  // Removes head
        System.out.println("Removed: " + removed);
        System.out.println("Remaining Queue: " + q);

    }
}

package set;

import java.util.*;

public class remove {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        TreeSet<Integer> uniqueNumbers = new TreeSet<>();
        System.out.println("Enter 5 numbers:");
        for (int i = 0; i < 5; i++) {
            int num = sc.nextInt();
            uniqueNumbers.add(num); // duplicates will be ignored
        }sc.close();
        System.out.println("Sorted Unique Numbers: " + uniqueNumbers);
    }
}

package arrays;

import java.util.*;

public class onedimensional {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter number of elements:");
        int size = sc.nextInt();
        int[] numbers = new int[size];
        System.out.println("enter" + size + "numbers");
        for(int i=0;i<size;i++){
            numbers[i] = sc.nextInt();
        }
        System.out.println("\nArray elements:");
        for (int i = 0; i < numbers.length; i++) {
            System.out.print(numbers[i] + " ");
        }
        numbers[0] +=10;
          int sum = 0;
        for (int num : numbers) {
            sum += num;
        }
        double average = (double) sum / size;

        System.out.println("\n\nAfter modifying first element: " + numbers[0]);
        System.out.println("Sum = " + sum);
        System.out.println("Average = " + average);
        sc.close();
    }
}

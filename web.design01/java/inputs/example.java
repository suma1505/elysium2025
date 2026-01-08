package inputs;

import java.util.*;

public class example {
        public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = sc.nextLine();
        System.out.print("Enter your age: ");
        int age = sc.nextInt();
        System.out.print("Enter your height: ");
        float height = sc.nextFloat();
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.printf("height: %.2f", height);
        sc.close();
    }
}

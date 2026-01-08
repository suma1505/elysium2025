package statements;

import java.util.*;

public class primenumber {
    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            System.out.println("enter number for n");
            int n = sc.nextInt();
            boolean isPrime = true;

        if (n <= 1) isPrime = false;
             else {
            for (int i = 2; i <= n / 2; i++) {
                if (n % i == 0) {
                    isPrime = false;
                    break;
                }
            }
        }
        sc.close();
        System.out.println(n + " is " + (isPrime ? "Prime" : "Not Prime"));
    }
}

package mathandWrapper;

import java.util.*;

public class power {
        public static void main(String[] args) {
        Scanner SC = new Scanner(System.in);
        System.out.print("Enter base: ");
        double base = SC.nextDouble();
        System.out.print("Enter exponent: ");
        double exp = SC.nextDouble();
        double result = Math.pow(base, exp);
        System.out.println("Result: " + result);
        SC.close();
    }
}

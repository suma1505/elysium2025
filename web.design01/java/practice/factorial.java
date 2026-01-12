package practice;

public class factorial {
    static int fact(int n) {
        int fact = 1;
        for (int i = 2; i <= n; i++) fact *= i;
        return fact;
    }

    public static void main(String[] args) {
        System.out.println("Factorial of 5: " + fact(5));
    }

}

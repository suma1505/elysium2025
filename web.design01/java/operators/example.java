package operators;

public class example {
        public static void main(String[] args) {
        int a = 10, b = 3;

        // Arithmetic
        System.out.println("Sum: " + (a + b));
        System.out.println("Remainder: " + (a % b));

        // Relational
        System.out.println("Is a > b? " + (a > b));
        // Logical
        boolean result = (a > b) && (b < 5);
        System.out.println("Logical AND result: " + result);

        // Assignment
        a += 2;
        System.out.println("Updated a: " + a);

        // Increment
        System.out.println("a++ = " + a++);
        System.out.println("Now a = " + a);
        // Bitwise
        System.out.println("a & b = " + (a & b));
    }
}

package mathandWrapper;

public class convert {
    public static void main(String[] args) {
        int num = 123;
        String str = Integer.toString(num); // int to String
        int parsed = Integer.parseInt(str); // String to int

        System.out.println("String: " + str);
        System.out.println("Parsed int: " + parsed);
    }

}

package practice;

public class count {
    public static void main(String[] args) {
        String str = "Hello Java";
        int count = 0;
        str = str.toLowerCase();
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if ("aeiou".indexOf(ch) != -1)
                count++;        }
        System.out.println("Vowels: " + count);
    }

}

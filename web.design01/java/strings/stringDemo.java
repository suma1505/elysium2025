package strings;

public class stringDemo {
    public static void main(String[] args) {
        String name = "Java Programming";
        System.out.println("Original: " + name);
        System.out.println("Length: " + name.length());
        System.out.println("Upper: " + name.toUpperCase());
        System.out.println("Trimmed: " + name.trim());
        System.out.println("Substring: " + name.substring(2, 6));
        System.out.println("Contains 'Pro': " + name.contains("Pro"));
        System.out.println("Replaced: " + name.replace("Java", "Python"));
    }
}

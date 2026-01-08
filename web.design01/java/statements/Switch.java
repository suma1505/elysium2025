package statements;

public class Switch {
    public static void main(String[] args) {
        int day = 3;
        switch (day) {
            case 1:
               System.out.println("sunday");
                break;
            case 2:
               System.out.println("monday");
                break;
            case 3:
               System.out.println("tuesday");
                break;    
            default:
               System.out.println("invalid");
        }
    }
}

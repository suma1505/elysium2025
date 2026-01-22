package errorhandling;

public class Age {
    public static class InvalidAgeException extends Exception {
        InvalidAgeException(String msg){
            super(msg);
        }
    }
  
     static void validate(int age) throws InvalidAgeException{
            if (age < 18) {
                throw new InvalidAgeException("Age must be 18+");
            }
    }
  
    public static void main(String[] args) {
        try {
            validate(17);
        } catch (InvalidAgeException e) {
            System.out.println(e.getMessage());
        }
    }
}

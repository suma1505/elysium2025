package errorhandling;

public class Atm {
    public static class InsufficientBalanceException extends Exception {
        InsufficientBalanceException(String msg) {
        super(msg);
        }
    }
        static void withdraw(int balance, int amount) throws InsufficientBalanceException {
            if (amount > balance)
                throw new InsufficientBalanceException("Insufficient Balance");
                System.out.println("Withdrawal Successful");
        }
 
    public static void main(String[] args) {
        try {
            withdraw(3000, 4000);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}

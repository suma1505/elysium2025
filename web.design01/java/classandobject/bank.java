package classandobject;

public class bank {
    public static class account {
        String name;
        int accnumber;
        double balance;

        account(String name,int accnumber,double balance){
            this.name = name;
            this.accnumber = accnumber;
            this.balance = balance;
        }
        void deposite(double amount){
            balance += amount;
            System.out.println("Deposited: " + amount);
        }
        void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
            System.out.println("Withdrawn: " + amount);
        } else {
            System.out.println("Insufficient Balance");
        }
        }   
        void displayBalance() {
        System.out.println("Account Holder: " + name);
        System.out.println("Account Number: " + accnumber);
        System.out.println("Current Balance: " + balance);
        System.out.println("-----------------------------");
        }
    }
    public static void main(String[] args) {
        account acc1 = new account("uma", 12345, 5000);
        acc1.displayBalance();
        acc1.deposite(1000);
        acc1.withdraw(2000);
        acc1.displayBalance();
    }
}

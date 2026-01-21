package oops;

import java.util.*;

public class PaymentMiniProject {
    public static abstract class payment {
        protected String userName;
        protected double amount;

        payment(String userName, double amount) {
            this.userName = userName;
            this.amount = amount;
        }

        abstract void pay();

        void showDetails() {
            System.out.println("customer name:" + userName);
            System.out.println("amount paid:" + amount);
        }

    }

    // upi payment
    public static class UPIPayment extends payment {
        private String upiId;

        UPIPayment(String userName, double amount, String upiId) {
            super(userName, amount);
            this.upiId = upiId;
        }

        @Override
        void pay() {
            showDetails();
            System.out.println("Payment method: UPI");
            System.out.println("UPI ID: " + upiId);
            System.out.println("Status : Payment successfull");
        }

    }

    // card payment
    public static class CardPayment extends payment {
        private String cardNumber;

        CardPayment(String userName, double amount, String cardNumber) {
            super(userName, amount);
            this.cardNumber = cardNumber;
        }

        @Override
        void pay() {
            showDetails();
            System.out.println("Payment method: Card");
            System.out.println("Card Number: **** **** **** " + cardNumber.substring(cardNumber.length() - 4));
            System.out.println("Status : Payment successfull");
        }
    }

    // net banking
    public static class NetBankingPayment extends payment {
        private String bankName;

        NetBankingPayment(String userName, double amount, String bankName) {
            super(userName, amount);
            this.bankName = bankName;
        }

        @Override
        void pay() {
            showDetails();
            System.out.println("Payment method: Net Banking");
            System.out.println("Bank Name: " + bankName);
            System.out.println("Status : Payment successfull");
        }
    }

    // cash payment
    public static class CashPayment extends payment {

        CashPayment(String userName, double amount) {
            super(userName, amount);
        }

        @Override
        void pay() {
            showDetails();
            System.out.println("Payment method: Cash");
            System.out.println("Status : Payment successfull");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("========PAYMENT SYSTEM========");

        System.out.println("Enter Customer Name:");
        String name = sc.nextLine();

        System.out.println("Enter Amount:");
        double amount = sc.nextDouble();

        System.out.println("\nSelect Payment Method:");
        System.out.println("1. UPI");
        System.out.println("1. UPI");
        System.out.println("2. Card");
        System.out.println("3. Net Banking");
        System.out.println("4. Cash");
        System.out.print("Enter choice: ");
        int choice = sc.nextInt();
        sc.nextLine(); 
        payment p = null;
        switch (choice) {
            case 1:
                System.out.print("Enter UPI ID: ");
                String upi = sc.nextLine();
                p = new UPIPayment(name, amount, upi);
                break;

            case 2:
                System.out.print("Enter Card Number: ");
                String card = sc.nextLine();
                p = new CardPayment(name, amount, card);
                break;

            case 3:
                System.out.print("Enter Bank Name: ");
                String bank = sc.nextLine();
                p = new NetBankingPayment(name, amount, bank);
                break;

            case 4:
                p = new CashPayment(name, amount);
                break;

            default:
                System.out.println("Invalid Payment Option");
                System.exit(0);
        }

        System.out.println("\n----- PAYMENT RECEIPT -----");
        p.pay();

        sc.close();
    }

}
package project;

import project.model.*;
import project.service.*;

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {

        List<Product> productList = new ArrayList<>();
        Set<Customer> customers = new HashSet<>();
        Map<Integer, Order> orderMap = new HashMap<>();

        Scanner sc = new Scanner(System.in);
        Payment payment = new CreditCardPayment();

        // Sample Products
        productList.add(new Product(1, "Laptop", 50000));
        productList.add(new Product(2, "Mobile", 20000));

        System.out.println("Enter your name:");
        String name = sc.nextLine();   // allows full name

        Customer customer = new Customer(name, name + "@mail.com");
        customers.add(customer);

        boolean running = true;

        while (running) {

            System.out.println("\n1. View Products");
            System.out.println("2. Buy Product");
            System.out.println("3. Save Orders");
            System.out.println("4. Exit");

            System.out.print("Enter choice: ");

            try {
                int choice = Integer.parseInt(sc.nextLine());

                switch (choice) {

                    case 1:
                        System.out.println("\nAvailable Products:");
                        productList.forEach(System.out::println);
                        break;

                    case 2:
                        System.out.print("Enter Product ID: ");
                        int pid = Integer.parseInt(sc.nextLine());

                        Product selected = productList.stream()
                                .filter(p -> p.getId() == pid)
                                .findFirst()
                                .orElseThrow(() -> new Exception("Product not found"));

                        payment.pay(selected.getPrice());

                        int orderId = orderMap.size() + 1;
                        Order order = new Order(orderId, selected, customer);
                        orderMap.put(orderId, order);

                        Orderthread thread = new Orderthread("Order ID " + orderId);
                        thread.start();

                        System.out.println("Order placed successfully!");
                        break;

                    case 3:
                        try (BufferedWriter writer =
                                     new BufferedWriter(new FileWriter("orders.txt",true))) {

                            for (Order o : orderMap.values()) {
                                writer.write(o.toString());
                                writer.newLine();
                            }

                            System.out.println("Orders Saved Successfully!");
                        }
                        break;

                    case 4:
                        running = false;
                        break;

                    default:
                        System.out.println("Invalid option. Please try again.");
                }

            } catch (NumberFormatException e) {
                System.out.println("Please enter a valid number.");
            } catch (Exception e) {
                System.out.println("Error: " + e.getMessage());
            }
        }

        sc.close();
        System.out.println("Application Closed.");
    }
}

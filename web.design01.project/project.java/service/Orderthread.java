package project.service;

public class Orderthread extends Thread{
    private String message;
        public Orderthread(String message) {
        this.message = message;
    }
    @Override
    public void run() {
        System.out.println("Processing order...");
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Order Completed: " + message);
    }
    
} 

package project.model;

import java.io.Serializable;

public class Order implements Serializable{
    private int orderId;
    private Product product;
    private Customer customer;

    public  Order(int orderId, Product product, Customer customer) {
        this.orderId = orderId;
        this.product = product;
        this.customer = customer;
    }
    @Override
    public String toString() {
        return "Order ID: " + orderId +
                ", Product: " + product +
                ", Customer: " + customer.getName() + customer.getEmail();
    }
}





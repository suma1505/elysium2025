package project.model;

import java.io.Serializable;

public class Customer extends Person implements Serializable {
    public Customer(String name, String email) {
        super(name, email);
    }

    @Override
    public void displayRole() {
        System.out.println("Role: Customer");
    }

}

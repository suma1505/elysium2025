package project.model;

import java.io.Serializable;

public abstract class Person implements Serializable{
    private String name;
    private String email;

    public  Person(String name, String email) {
        this.name = name;
        this.email = email;
    }

    public String getName() {
        return name;
    }
    public String getEmail() {
        return email;
    }

    public abstract void displayRole();

}

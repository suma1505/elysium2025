package oops;

public class EmployeeMiniProject {
    public static class employee {
        private int empid;
        private String name;
        private double amount;

        employee(int empid, String name, double amount){
            this.empid = empid;
            this.name = name;
            this.amount = amount;
        }
        void displayDetails() {
        System.out.println("ID: " + empid);
        System.out.println("Name: " + name);
        System.out.println("Salary: " + amount);
        }
    }
    public static class manager extends employee {
        private String department;
        manager(int empid, String name, double amount, String department) {
            super(empid, name, amount);
            this.department = department;
        }
        @Override
        void displayDetails() {
            super.displayDetails();
            System.out.println("Department: " + department);
        }
    }
    public static class engineer extends employee {
        private String skill;
        engineer(int empid, String name, double amount, String skill) {
        super(empid, name, amount);
        this.skill = skill;
        }
        @Override
        void displayDetails() {
            super.displayDetails();
            System.out.println("Skill: " + skill);
        }
    }
    public static void main(String[] args) {
        employee e1 = new manager(101, "uma", 50000, "HR");
        employee e2 = new engineer(102, "prarthana", 40000, "Java");

        e1.displayDetails();
        System.out.println("----------------");
        e2.displayDetails();
    }
}



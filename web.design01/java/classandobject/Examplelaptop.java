package classandobject;

public class Examplelaptop {
    public static class laptop {
        String brand;
        double price;

        laptop(String brand,double price){
            this.brand = brand;
            this.price = price;
        }
        void showDetails() {
        System.out.println("Laptop Brand: " + brand);
        System.out.println("Price: " + price);
        }
    }
    public static void main(String[] args) {
        laptop l1 = new laptop("Dell", 75000);
        laptop l2 = new laptop("HP", 68000);
        l1.showDetails();
        l2.showDetails();
    }
}

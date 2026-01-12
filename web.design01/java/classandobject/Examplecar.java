package classandobject;

public class Examplecar {
    public static class car {
        String brand;
        String model;
        int year;

        car(String brand, String model,int year){
            this.brand = brand;
            this.model = model;
            this.year = year;
        }
        void displayDetails(){
            System.out.println("brand:"+ brand);
            System.out.println("model:"+ model);
            System.out.println("year:"+ year);
            System.out.println("------------------");
        }
    }
        public static void main(String[] args) {
            car c1 = new car("toyota","camry",2022);
            car c2 = new car("huyndai","venue",2023);
            c1.displayDetails();
            c2.displayDetails();
        }
}
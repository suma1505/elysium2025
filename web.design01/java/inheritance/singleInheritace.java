package inheritance;

public class singleInheritace {
    public static class animal {
        void eat(){
            System.out.println("animal is eating");
        }
    }
    public static class dog extends animal {
        void bark(){
            System.out.println("barking");
        }  
    }
    public static void main(String[] args) {
        dog d = new dog();
        d.eat();
        d.bark();
    }
}

package encapsulation;

public class ExampleAbstract {
    public static abstract class animal {
        abstract void sound();
        void sleep(){
            System.out.println("Sleeping");
        }
    }
    public static class dog extends animal {
        @Override
        void sound(){
            System.out.println("dog barks");
        }
    }
    public static class cat extends animal {
        @Override
        void sound(){
            System.out.println("cat meows");
        }
    }
    public static void main(String[] args) {
        animal a1 = new dog();
        animal a2 = new cat();
        a1.sound();
        a1.sleep();
        a2.sound();
        a2.sleep();
    }
}

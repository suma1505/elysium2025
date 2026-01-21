package polymorphism;

public class overRiding {
    public static class animal {
        void sound(){
            System.out.println("animal makes sound");
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
            System.out.println("cat meoww");
        }
        
    }
    public static void main(String[] args) {
        animal a;
        a = new dog();
        a.sound();
        a = new cat();
        a.sound();
    }
}

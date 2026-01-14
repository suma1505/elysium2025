package inheritance;

public class hierarchical {
    public static class animal {
        void sound(){
            System.out.println("animal makes sound");
        }
    }
    public static class dog extends animal {
        void bark(){
            System.out.println("dog is barking");
        }
    }
    public static class puppy extends animal {
        void weep(){
            System.out.println("puppy is weeping");
        }
    }
    public static void main(String[] args) {
        puppy p = new puppy();
        p.weep();
        p.sound();
        dog d = new dog();
        d.bark();
        d.sound();
    }
}

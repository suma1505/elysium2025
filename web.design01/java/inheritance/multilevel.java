package inheritance;

public class multilevel {
    public static class animal {
        void eat(){
            System.out.println("Eating");
        }
    }
    public static class dog extends animal {
        void bark(){
            System.out.println("Barking");
        }
    }
    public static class puppy extends dog {
        void weep(){
            System.out.println("Weeping");
        }
    }
    public static void main(String[] args) {
        puppy p = new puppy();
        p.weep();
        p.bark();
        p.eat();
    }
}

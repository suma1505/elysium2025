package inheritance;

public class multiple {
    public static interface A {
        void methodA(); 
    } 
    public static interface B {
        void methodB();
    }
    public static class C implements A, B {
        public void methodA(){
            System.out.println("Method A");
        }
         public void methodB(){
            System.out.println("Method B");
        }
    }
    public static void main(String[] args) {
        C c=new C();
        c.methodA();
        c.methodB();
    }
}

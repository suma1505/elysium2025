package inheritance;

public class hybrid {
    public static interface printable {
        void print();  
    }
    public static interface showable {
        void show();
    }
    public static class A {
        void message(){
            System.out.println("class A method");
        }
    }
    public static class demo extends A implements printable, showable {
        public void print(){
            System.out.println("printable interface");
        }
        public void show(){
            System.out.println("showable interface");
        }
    }
    public static void main(String[] args) {
        demo d = new demo();
        d.show();
        d.print();
        d.message();
    }
}

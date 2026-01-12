package classandobject;

public class rectangle {
    public static class rect {
        int length;
        int breadth;
        
        rect(int length, int breadth){
            this.length = length;
            this.breadth = breadth;
        }
        int area(){
            return length * breadth;
        }
    }
        public static void main(String[] args) {
            rect r1 = new rect(5,10);
            rect r2 = new rect(4,7);
        System.out.println("Area of Rectangle 1: " + r1.area());
        System.out.println("Area of Rectangle 2: " + r2.area());
    }
}

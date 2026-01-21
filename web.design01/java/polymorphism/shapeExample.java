package polymorphism;

public class shapeExample {
    public static class shape {
        void area(){
            System.out.println("area of shape is undefined");
        }
    }
    public static class circle extends shape {
        double radius = 5;
        @Override
        void area(){ 
            double result= Math.PI * radius * radius;
            System.out.println("area of circle :"+result);
        }
    }
      public static class square extends shape {
        int side =4;
        @Override
        void area(){ 
            int result= side*side;
            System.out.println("area of square :"+result);
        }
    }
      public static class rectangle extends shape {
        int base = 5;
        int height = 3;
        @Override
        void area(){ 
            double result= 0.5*base*height;
            System.out.println("area of rectangle :"+result);
        }
    }
    public static void main(String[] args) {
        shape s;
        s = new circle();
        s.area();
        s = new rectangle();
        s. area();
        s= new square();
        s.area();
    }
}

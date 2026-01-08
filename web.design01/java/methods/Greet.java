package methods;

public class Greet {
    void display(){
        System.out.println("welcome to java methods");
    }
    void add(int a,int b){
        System.out.println("sum ofa and b is:"+(a+b));
    }
    double add(double a,int b){
        return a+b;
    }
    public static void main(String[] args) {
       Greet g1=new Greet();
       g1.display();
       g1.add(10,20);
       double res=g1.add(5.5,5);
       System.out.println("sum of a and b is "+res);

    }
}

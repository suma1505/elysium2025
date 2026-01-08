package methods;

public class calculator {
    void greet(){
        System.out.println("welcome to java methods");
    }
    int add(int a, int b){
        return a + b;
    }
    int sub(int a, int b){
        return a - b;
    }
    double add(double a, double b){
        return a + b;
    }
    public static void main(String[] args) {
       calculator calc = new calculator();
       calc.greet();
       int res = calc.add(5, 10);
       System.out.println("sum of a and b is:"+(res));
       double result = calc.add(5.4,4.5);
       System.out.println("sum of a and b is:"+(result));
        int diff = calc.sub(5, 10);
       System.out.println("diff of a and b is:"+(diff));
    }
}

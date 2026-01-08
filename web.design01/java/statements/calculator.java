package statements;

import java.util.*;

public class calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter two numbers:");
        double a=sc.nextDouble();
        double b=sc.nextDouble();

        System.out.println("choose operator(+,-,*,/):");
        char op = sc.next().charAt(0);
        sc.close();
        switch (op) {
            case '+':
                System.out.println("sum:"+(a+b));
                break;
            case '-':
                System.out.println("sub:"+(a-b));
                break;
            case '*':
                System.out.println("multiply:"+(a*b));
                break;
            case '/':
                System.out.println("divide:"+(a/b));
                break;  
            default:
                System.out.println("invalid");
        }
    }
   
}

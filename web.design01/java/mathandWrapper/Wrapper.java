package mathandWrapper;

public class Wrapper {
    
    public static void main(String[] args) {
        int a = 10;
        Integer obj = Integer.valueOf(a);  
        int b = obj.intValue();            
        
        Integer x = a;      
        int y = x;           
        System.out.println(x + ", " + y); 
        System.out.println(b); 
    }
}

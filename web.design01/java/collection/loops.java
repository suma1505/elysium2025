import java.util.*;

public class loops {
    public static void main(String[] args) {
        List <String> colors=new ArrayList<>(Arrays.asList("red","blue","green"));
        System.out.println(colors);
         System.out.println("===================");
    //for loop
    for(int i=0;i<colors.size();i++){
            System.out.println("Color name:"+colors.get(i));
        }
        System.out.println("===================");
        // enhanced for loop
        for(String c:colors){
            System.out.println(c);
        }
        System.out.println("===================");

        // foreach loop

        colors.forEach(c->System.out.println(c));
        System.out.println("===================");
        //itrator
        Iterator<String> f=colors.iterator();
        while(f.hasNext()){
            System.out.println(f.next());
        }
    }
}

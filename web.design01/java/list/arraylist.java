package list;

import java.util.*;


public class arraylist {
    public static void main(String[] args) {
        List <String> l = new ArrayList<>();

        // add elements
        l.add("apple");
        l.add("banana");
        System.out.println(l);

         // add in specific index
        l.add(1, "mango");
        System.out.println(l);

         // get element
        System.out.println(l.get(0));

        // set element
        l.set(0, "orange");
        System.out.println(l);

        // remove by index
        l.remove(1);
        System.out.println(l);
       
         // remove by value  
        l.remove("banana");
        System.out.println(l);
        
        // check contains
        System.out.println(l.contains("orange"));

        // get size
        System.out.println(l.size());

        // sort list
        Collections.sort(l);
        System.out.println(l);

        // clear list
        l.clear();
        System.out.println(l);
    }
}

package map;

import java.util.HashMap;

public class map {
    public static void main(String[] args) {
        HashMap<Integer, String> map = new HashMap<>();

        map.put(1, "Apple");
        map.put(2, "Banana");
        map.put(3, "Mango");

        System.out.println(map.get(2)); 

        map.put(2, "Orange"); 

        System.out.println(map.containsKey(3));
        System.out.println(map.containsValue("Apple")); 
        map.remove(1); 
        System.out.println(map.size());
     
        for (Integer key : map.keySet()) {
            System.out.println(key + " => " + map.get(key));
        }
        map.clear();
    }
}

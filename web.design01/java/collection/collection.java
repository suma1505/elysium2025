import java.util.*;

public class collection {

    public static void main(String[] args) {
        // list

        List <String> list = new ArrayList<>(Arrays.asList("apple","orange","mango"));
        list.add("watermelon");
        list.add("grapes");
        System.out.println(list);
        System.out.println("====================");
        List <Integer> num = new LinkedList<>();
        num.add(101);
        num.addFirst(100);
        num.addLast(102);
        System.out.println(num);
        System.out.println("=====================");

        // set

        Set<String> fruits = new HashSet<>();
        fruits.add("apple");
        fruits.add("mango");
        fruits.add("orange");
        fruits.add("apple");
        fruits.add("mango");
        System.out.println(fruits);
        System.out.println("======================");

        // map
        Map<String,String> person = new HashMap<>();
        person.put("name", "uma");
        System.out.println(person);
    }
}
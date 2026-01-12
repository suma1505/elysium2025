package classandobject;

public class object {
    public static class Student {
        int id;
        String name;

        void display() {
            System.out.println(id + " " + name);
        }
    }

    public static void main(String[] args) {
        Student s1 = new Student();
        Student s2 = new Student();
        s1.id = 101;
        s1.name = "user";
        s2.id = 102;
        s2.name = "admin";
        s1.display();
        s2.display();
    }
}

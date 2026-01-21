package encapsulation;

public class ExampleStudent {
    public static class student {
        private String name;
        private int age;

        public String getName(){
            return name;
        }
          public int getAge(){
            return age;
        }

        public void setName(String name){
            this.name = name;
        }
         public void setAge(int age){
            if (age>0) {
                this.age = age;
            }
            else{
                System.out.println("age must be positive");
            }
        }
    }
    public static void main(String[] args) {
        student s = new student();
        s.setName("uma");
        s.setAge(21);

        System.out.println("name:"+s.getName());
        System.out.println("age:"+s.getAge());
    }
}

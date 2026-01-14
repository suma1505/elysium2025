package inheritance;

public class miniProgram {
    public static class student {
        String name;
        int roll;
        student(String name, int roll){
            this.name = name;
            this.roll = roll;
        }
        void showDetails(){
            System.out.println(name);
            System.out.println(roll);
        }
    }
    public static class result extends student {
        int marks1, marks2;
        result(String name, int roll, int m1,int m2){
            super(name, roll);
            this.marks1= m1;
            this.marks2 =m2;
        }
        void shoeResult(){
            super.showDetails();
            int total = marks1 + marks2;
            System.out.println("total marks:"+ total);
        }
    }
    public static void main(String[] args) {
        result r = new result("uma", 101, 75, 80);
        result r1 = new result("prarthana", 102, 98, 95);
        r.shoeResult();
        r1.shoeResult();
    }
}
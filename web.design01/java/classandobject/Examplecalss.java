package classandobject;

public class Examplecalss {
    public static class Emp {
             int id;
             String name,city,position;
             double salary;

             Emp(int id,String name,String city,String position,double salary){
                this.id=id;
                this.name=name;
                this.city=city;
                this.position=position;
                this.salary=salary;
             }
             void Show(){
                System.out.println("emp id:"+id);
                System.out.println("emp name:"+name);
                System.out.println("emp city:"+city);
                System.out.println("emp position:"+position);
                System.out.println("emp sal:"+salary);
                System.out.println("------------------------------------");
             }
        
    }
    public static void main(String[] args) {
        Emp e1=new Emp(101, "admin", "trichy", "developer", 20000.00);
        Emp e2=new Emp(102, "user", "madurai", "HR", 30000.00);
        e1.Show();
        e2.Show();

    }
}

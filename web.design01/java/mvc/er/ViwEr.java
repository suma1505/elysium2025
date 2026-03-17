public class ViwEr extends CtrlEr {

public static void main(String[] args) {

ViwEr obj=new ViwEr();

obj.setRno(1001);
obj.setSname("x5");
obj.setM1(56.5);
obj.setM2(63);

System.out.println(obj.getRno());
System.out.println(obj.getSname());
System.out.println(obj.getM1());
System.out.println(obj.getM2());
System.out.println(obj.getTotal());
System.out.println(obj.getAverage());
System.out.println(obj.getResult());

System.out.println("----------");

System.out.println(obj);
}

}
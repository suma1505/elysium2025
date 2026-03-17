public class CtrlEr extends MdlEr {

public double getTotal() {
	return getM1() + getM2();
}

public double getAverage() {
	return (getTotal()) / 2;
}

public String getResult() {
	return (getM1() > 34.4 && getM2() > 34.4 ? "Pass" : "Fail");
}


public String toString() {

	String op="";

	op += String.format("Roll no.: %d\n", getRno());
	op += String.format("Student Name: %s\n", getSname());
	op += String.format("Mark-1: %.2f\n", getM1());
	op += String.format("Mark-2: %.2f\n", getM2());
	op += String.format("Total: %.2f\n", getTotal());
	op += String.format("Average: %.2f\n", getAverage());
	op += String.format("Result: %s\n", getResult());

	return op;
}

}
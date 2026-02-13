package thread;

class PrintNumber extends Thread{
    public void run(){
        for(int i=1;i<=5;i++){
            System.out.println("Number"+i);
        }
        try {
            Thread.sleep(800);
        } catch (InterruptedException e) {
            System.out.println("Error");
        }
    }
} 
class PrintLetter implements Runnable{
    public void run(){
        for(char i='A';i<='E';i++){
            System.out.println("Letter"+i);
        }
        try {
            Thread.sleep(200);
        } catch (InterruptedException e) {
            System.out.println("Error");
        }
    }
}

public class TherdDemo {
    public static void main(String[] args) throws InterruptedException {
        PrintNumber t1=new PrintNumber();
        PrintLetter l1=new PrintLetter();
        Thread t2=new Thread(l1);
        t2.start();
        t2.join();
        t1.start();
        
    }
    
}

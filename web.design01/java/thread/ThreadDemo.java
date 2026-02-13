package thread;

class PrintNumber extends Thread{
    public void run(){
        for(int i=1;i<=8;i++){
            System.out.println("numbers:"+i);
        }
        try {
            Thread.sleep(500);          
        } catch (Exception e) {
            System.out.println("error");
        }
    }
}

class PrintLetter implements Runnable{
    public void run(){
        for(char ch='A';ch<='G';ch++){
            System.out.println("letters:"+ch);
        }
        try {
            Thread.sleep(1000);          
        } catch (Exception e) {
            System.out.println("error");
        }
    }
}
public class ThreadDemo {
    public static void main(String[] args) {
       PrintNumber t1 = new PrintNumber();
       Thread t2 = new Thread(new PrintLetter());
       t1.start();
       t2.start();
    }
}

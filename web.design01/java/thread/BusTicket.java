package thread;

public class BusTicket implements Runnable{
    static int total = 8;
    int ticketneed;

    BusTicket( int ticketneed){
        this.ticketneed=ticketneed;
    }

    @Override
    public void run(){
        synchronized (BusTicket.class){
            String name = Thread.currentThread().getName();
            System.out.println(name + "ticketneeded" + ticketneed + "tickets");

            if (ticketneed<=total) {
                System.out.println(name + "try to book" + ticketneed +"tickets");
                total=total-ticketneed;
                System.out.println(ticketneed + "tickets booked succcess");
                System.out.println("tickets left:" + total);
            }else{
                System.out.println("sorry tickets sold out");
            }
            try {
                Thread.sleep(800);
            } catch (Exception e) {
               System.out.println("error");
            }
        }
    }

    public static void main(String[] args) {
        BusTicket uma = new BusTicket(2);
        BusTicket prarthana = new BusTicket(3);
        BusTicket sneha = new BusTicket(2);
        Thread t1 = new Thread(uma,"uma");
        Thread t2 = new Thread(prarthana,"prarthana");
        Thread t3 = new Thread(sneha,"sneha");
        t1.start();
        t2.start();
        t3.start();
    }
}

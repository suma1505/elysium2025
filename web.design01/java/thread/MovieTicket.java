package thread;

public class MovieTicket implements Runnable {
    static int total = 10;
    int ticketneed;

    MovieTicket(int ticketneed) {
        this.ticketneed = ticketneed;
    }

    @Override
    public void run() {
        synchronized (MovieTicket.class) {
            String name = Thread.currentThread().getName();
            System.out.println(name + "needed " + ticketneed + "tickets");

            if (ticketneed <= total) {
                System.out.println(name + "try to book" + ticketneed +"tickets");
                total = total - ticketneed;
                System.out.println(ticketneed + "booked tickets success");
                System.out.println("Tickets Left" + total);
            } else {
                System.out.println("sorry tickets sold out");
            }
            try {
                Thread.sleep(1000);
            } catch (Exception e) {
                System.out.println("Error");
            }
        }
    }

    public static void main(String[] args) {
        MovieTicket sundar = new MovieTicket(2);
        MovieTicket arun = new MovieTicket(5);
        MovieTicket santhose = new MovieTicket(2);
        MovieTicket sam=new MovieTicket(1);
        Thread t1 = new Thread(sundar, "sundar");
        Thread t2 = new Thread(arun, "arun");
        Thread t3 = new Thread(santhose, "santhose");
        Thread t4=new Thread(sam,"sam");
        
        t1.start();
        t2.start();
        t3.start();
        t4.start();
    }

}

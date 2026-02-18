import java.sql.*;

class TicketCounter{
    String url = "jdbc:mysql://localhost:3306/ticketdb";
    String username= "root";
    String password = "";

    public void bookTicket(String user, int requestedTickets){
        Connection con=null;
        try {
            con = DriverManager.getConnection(url,username,password);
            con.setAutoCommit(false);

            String selectQuery = "select available_tickets from busticket where id = 1 for update";
            PreparedStatement ps= con.prepareStatement(selectQuery);
            ResultSet rs = ps.executeQuery();

            if (rs.next()) {
                int available = rs.getInt("available_tickets");

                System.out.println(user + " trying to book " + requestedTickets + " tickets");

                if (available >= requestedTickets) {

                    Thread.sleep(1000); 

                     int remaining = available - requestedTickets;

                    String updateQuery = "update busticket set available_tickets = ? where id = 1";
                    PreparedStatement ps1 = con.prepareStatement(updateQuery);
                    ps1.setInt(1, remaining);
                    ps1.executeUpdate();

                    con.commit();

                    System.out.println(user + " booked successfully. Remaining: " + remaining);
                } else {
                    System.out.println("Sorry " + user + ", Not enough tickets. Remaining: " + available);
                    con.rollback();
                }
            }
        } catch (Exception e) {
           e.printStackTrace();
        }
    }

}

class UserThread extends Thread{
    private TicketCounter counter;
    private String name;
    private int requestedTickets;

     UserThread(TicketCounter counter, String name, int requestedTickets) {
        this.counter = counter;
        this.name = name;
        this.requestedTickets = requestedTickets;
    }

    public void run() {
        synchronized(TicketCounter.class){
           counter.bookTicket(name, requestedTickets);
        }
    }
}
public class Ticketsystem1 {
    public static void main(String[] args) {
        TicketCounter counter = new TicketCounter();

        Thread t1 = new UserThread(counter, "prarthana", 2);
        Thread t2 = new UserThread(counter, "varsha", 4);
        Thread t3 = new UserThread(counter, "viji", 1);
        Thread t4 = new UserThread(counter, "uma", 2);

        t1.start();
        t2.start();
        t3.start();
        t4.start();
    }
}


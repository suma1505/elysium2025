import java.sql.*;

class TicketCounter {

    String URL = "jdbc:mysql://localhost:3306/ticketdb";
    String USER = "root";
    String PASSWORD = "";

    public void bookTicket(String user, int requestedTickets) {

        Connection con = null;
 
        try {
            con = DriverManager.getConnection(URL, USER, PASSWORD);

            // Start transaction
            con.setAutoCommit(false);

            // Lock the row to prevent race condition
            String selectQuery = "SELECT available_tickets FROM tickets WHERE id = 1 FOR UPDATE";
            PreparedStatement ps1 = con.prepareStatement(selectQuery);
            ResultSet rs = ps1.executeQuery();

            if (rs.next()) {
                int available = rs.getInt("available_tickets");

                System.out.println(user + " trying to book " + requestedTickets + " tickets");

                if (available >= requestedTickets) {

                    Thread.sleep(1000); // simulate delay

                     int remaining = available - requestedTickets;

                    String updateQuery = "UPDATE tickets SET available_tickets = ? WHERE id = 1";
                    PreparedStatement ps2 = con.prepareStatement(updateQuery);
                    ps2.setInt(1, remaining);
                    ps2.executeUpdate();

                    con.commit(); // commit transaction

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

class UserThread extends Thread {

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

public class TicketSystem {

    public static void main(String[] args) {

        TicketCounter counter = new TicketCounter();

        Thread t1 = new UserThread(counter, "User1", 5);
        Thread t2 = new UserThread(counter, "User2", 3);
        Thread t3 = new UserThread(counter, "User3", 5);
        Thread t4 = new UserThread(counter, "User4", 3);

        t1.start();
        t2.start();
        t3.start();
        t4.start();
    }
}

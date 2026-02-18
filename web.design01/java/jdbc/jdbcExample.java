import java.sql.*;
public class jdbcExample {

    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/schooldb";
        String username = "root";
        String password ="";

        try {
            Connection con = DriverManager.getConnection(url, username,password);
            System.out.println("db connection success");
            Statement stmt = con.createStatement();

            String insertquery = "insert into students(name, age, dept) values('uma',21,'computer science')";
            stmt.executeUpdate(insertquery);
            System.out.println("data inserted");

            String selectquery = "select * from students";
            ResultSet rs = stmt.executeQuery(selectquery);

            System.out.println("student details");
            while (rs.next()) {
                System.out.println(
                    rs.getInt("id") +"|"+
                    rs.getString("name") +"|"+
                    rs.getInt("age") +"|"+
                    rs.getString("dept")

                );
            }
            con.close();
            System.out.println("connection closed");

        } catch (Exception e) {
           e.printStackTrace();
        }
        
    }
}
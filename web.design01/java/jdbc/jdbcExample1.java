import java.sql.*;

public class jdbcExample1 {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/company_db";
        String username = "root";
        String password ="";

        try {
            Connection con = DriverManager.getConnection(url,username,password);
            System.out.println("db connected success");
            Statement stmt = con.createStatement();

            String insertquery = "insert into employees (name, salary) values ('sneha', 35000)";
            stmt.executeUpdate(insertquery);
            System.out.println("query insert success");

            String selectquery = "select * from employees";
            ResultSet rs = stmt.executeQuery(selectquery);

            System.out.println("employee details");
            while (rs.next()) {
                System.out.println(
                    rs.getInt("id") + "|" +
                    rs.getString("name") + "|" +
                    rs.getDouble("salary")
                );
            }
            con.close();
            System.out.println("connection closed");

        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}

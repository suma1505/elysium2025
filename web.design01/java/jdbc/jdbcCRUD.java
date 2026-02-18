import java.sql.*;;

public class jdbcCRUD {
    public static void main(String[] args) {

        String url = "jdbc:mysql://localhost:3306/schooldb";
        String username = "root";
        String password ="";

        try {
            Connection con = DriverManager.getConnection(url,username,password);
            System.out.println("db connected success");
            Statement stmt = con.createStatement();

        String sql = "insert into student(name, marks) values (?, ?)";
        PreparedStatement ps = con.prepareStatement(sql);
        ps.setString(1, "prarthana");
        ps.setDouble(2, 83.5);

        int row = ps.executeUpdate();
        System.out.println(row + " row inserted");

        String sql1 = "select * from student";
        PreparedStatement ps1 = con.prepareStatement(sql1);
        ResultSet rs = ps1.executeQuery();

        while (rs.next()) {
            System.out.println(
                    rs.getInt("id") + " " +
                            rs.getString("name") + " " +
                            rs.getDouble("marks"));
        }

       

        String sql3 = "update student set marks = ? where id = ?";
        PreparedStatement ps3 = con.prepareStatement(sql3);
        ps3.setDouble(1, 90);
        ps3.setInt(2, 1);

        int row1 = ps3.executeUpdate();
        System.out.println(row1 + " row updated");

         String sql2 = "select * from student where id = ?";
        PreparedStatement ps2 = con.prepareStatement(sql2);
        ps2.setInt(1, 1);

        ResultSet rs1 = ps2.executeQuery();
        System.out.println("updated data"+ rs1);

        String sql4 = "delete from student where id = ?";
        PreparedStatement ps4 = con.prepareStatement(sql4);
        ps4.setInt(1, 1);

        int row2 = ps4.executeUpdate();
        System.out.println(row2 + " row deleted");
        con.close();
        System.out.println("connection closed");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

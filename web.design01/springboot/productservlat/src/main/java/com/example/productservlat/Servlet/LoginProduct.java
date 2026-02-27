package com.example.productservlat.Servlet;

import com.example.productservlat.util.DBConnection;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

@WebServlet("/loginproduct")
public class LoginProduct extends HttpServlet {
    public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException{
        String name=request.getParameter("name");
        double price=Double.parseDouble(request.getParameter("price"));
        try{
            Connection con = DBConnection.getConnection();
            PreparedStatement ps = con.prepareStatement("select * from product where name=? and price=?");
            ps.setString(1,name);
            ps.setDouble(2,price);

            ResultSet rs =ps.executeQuery();

            if(rs.next()){
                HttpSession session=request.getSession();
                session.setAttribute("name",name);
                response.sendRedirect("/home");
            }else {
                response.sendRedirect("/login");
            }
        }catch(Exception e) {
            e.printStackTrace();
        }

    }
}

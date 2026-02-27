package com.example.productservlat.Servlet;

import com.example.productservlat.util.DBConnection;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;

@WebServlet("/registerproduct")
public class RegisterProduct extends HttpServlet {
    public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException{
        String name = request.getParameter("name");
        String des = request.getParameter("des");
        int qty = Integer.parseInt(request.getParameter("qty"));
        double price = Double.parseDouble(request.getParameter("price"));
        try{
            Connection con = DBConnection.getConnection();
            PreparedStatement ps = con.prepareStatement("insert into product(name,des,qty,price)values(?,?,?,?)");
            ps.setString(1,name);
            ps.setString(2,des);
            ps.setInt(3,qty);
            ps.setDouble(4,price);
            ps.executeUpdate();
            response.sendRedirect("/login");
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

    }
}

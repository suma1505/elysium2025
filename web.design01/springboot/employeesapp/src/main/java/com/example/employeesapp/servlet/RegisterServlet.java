package com.example.employeesapp.servlet;


import com.example.employeesapp.util.DBConnection;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;

@WebServlet("/registeremployee")
public class RegisterServlet extends HttpServlet {
    public  void doPost(HttpServletRequest request,
                        HttpServletResponse response) throws IOException, ServletException {
        String name = request.getParameter("name");
        String email = request.getParameter("email");
        String password=request.getParameter("password");
        try {
            Connection con= DBConnection.getConnection();
            PreparedStatement ps=con.prepareStatement("insert into students(name,email,password) values(?,?,?)");
            ps.setString(1,name);
            ps.setString(2,email);
            ps.setString(3,password);
            ps.executeUpdate();
            response.sendRedirect("/login");
        } catch (Exception e) {
                e.printStackTrace();
        }
    }
}


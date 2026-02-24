package com.example.employeesapp.servlet;

import com.example.employeesapp.util.DBConnection;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import javax.sql.rowset.serial.SerialException;
import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

@WebServlet("/loginemployee")
public class LoginServlet extends HttpServlet {
    public  void doPost(HttpServletRequest request,
                        HttpServletResponse response) throws IOException, ServletException {
        String email=request.getParameter("email");
        String password=request.getParameter("password");
        try{
            Connection con = DBConnection.getConnection();
            PreparedStatement ps=con.prepareStatement("select * from employees where email=? and password=?");
            ps.setString(1,email);
            ps.setString(2,password);

            ResultSet rs=ps.executeQuery();

            if(rs.next()){
                response.sendRedirect("/success");
            }else{
                response.sendRedirect("/");
            }

        }catch(Exception e){
            e.printStackTrace();
        }
    }
}


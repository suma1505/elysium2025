package com.example.servletDemo;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;

@WebServlet
public class servlet extends HttpServlet {

    protected void doGet(HttpServletRequest request,
                            HttpServletResponse response)
                    throws ServletException, IOException {
                response.setContentType("text/HTML");
                PrintWriter out = response.getWriter();
                out.println("<h1>Hello from this is servlet demo in spring</h1>");
    }
}

package com.example.servletDemo;

import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@WebServlet("/demo")
public class Demoservlet extends servlet{
    public void init() {

        System.out.println("Servlet Initialized");
    }

    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response) {
        System.out.println("Request handled");
    }

    public void destroy() {

        System.out.println("Servlet Destroyed");
    }
}


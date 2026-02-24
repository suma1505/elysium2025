package com.example.employeesapp.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

import java.sql.Connection;

@Controller
public class PageController {
    @GetMapping("/register")
    public String registerpage(){
        return "register";
    }
    @GetMapping("/login")
    public String loginpage(){
        return "login";
    }
    @GetMapping("/success")
    public  String successpage(){
        return "success";
    }

}

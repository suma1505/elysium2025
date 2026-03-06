package com.example.roleaccess.controller;

import com.example.roleaccess.model.User;
import com.example.roleaccess.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;


@RestController
public class UserController {

    @Autowired
    private UserService service;

    @PostMapping("/register")
    public User register(@RequestBody User user){
        return service.Register(user);
    }

    @GetMapping("/user")
    public String user(){
        return  "user access";
    }

    @GetMapping("/admin")
    public  String admin(){
        return  "admin access";
    }
}

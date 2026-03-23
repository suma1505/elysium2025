package com.example.security.controller;

import com.example.security.dto.UserRequest;
import com.example.security.model.User;
import com.example.security.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
public class AuthController {

    @Autowired
    private UserService service;

    @PostMapping("/register")
    public User register(@RequestBody UserRequest request) {

        return service.register(request);
    }

    @GetMapping("/user")
    public String userApi() {

        return "User Access";
    }

    @GetMapping("/admin")
    public String adminApi() {

        return "Admin Access";
    }
}
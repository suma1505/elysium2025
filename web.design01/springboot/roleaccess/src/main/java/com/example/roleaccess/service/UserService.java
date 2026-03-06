package com.example.roleaccess.service;


import com.example.roleaccess.model.User;
import com.example.roleaccess.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class UserService {

    @Autowired
    private UserRepository repo;

    @Autowired
    private PasswordEncoder encoder;

    public User Register(User user){
        User U=new User();

        U.setUsername(user.getUsername());
        U.setRole(user.getRole());
        U.setPassword(encoder.encode(user.getPassword()));

        return repo.save(U);
    }
}

package com.example.author.service;

import com.example.author.model.User;
import com.example.author.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    @Autowired
    private UserRepository repo;

    public  String registerUser(User user){
        User exists= repo.findByEmail(user.getEmail());

        if(exists!=null){
            return "email already exists";
        }else {
            repo.save(user);
        }
        return "register success";
    }

    public String loginUser(User user){
        User exists=repo.findByEmail(user.getEmail());

        if(exists==null){
            return "user not found";
        }
        if(user.getPassword().equals(exists.getPassword())){
            return "login success";
        }
        return "invalid password";
    }
}

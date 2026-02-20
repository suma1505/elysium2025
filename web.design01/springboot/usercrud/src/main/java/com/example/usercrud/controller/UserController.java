package com.example.usercrud.controller;

import com.example.usercrud.model.User;
import com.example.usercrud.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/user")
public class UserController {

    @Autowired
    private UserRepository repo;

    @PostMapping
    public User adduser(@RequestBody User user){
        return  repo.save(user);
    }

    @GetMapping
    public List<User> gatall(){
        return  repo.findAll();
    }

    @PutMapping("/{id}")
    public User updateuser(@PathVariable Long id,@RequestBody User user){
        User u= repo.findById(id).orElseThrow();

        u.setName(user.getName());
        u.setEmail(user.getEmail());
        u.setPassword(user.getPassword());

        return  repo.save(u);
    }

    @DeleteMapping("/{id}")
    public  String deleteuser(@PathVariable Long id){
        repo.deleteById(id);
        return  "user deleted";
    }

}

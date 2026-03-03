package com.example.productcrud.controller;

import com.example.productcrud.model.Product;
import com.example.productcrud.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.util.List;

@RestController
@RequestMapping("/api/products")
@CrossOrigin("*")
public class ProductController {

    @Autowired
    private ProductService service;


    @PostMapping
    public Product addproduct(@RequestParam String name, @RequestParam double price, @RequestParam String des, @RequestParam MultipartFile image){
        return service.addproduct(name,price,des,image);

    }

    @GetMapping
    public List<Product> getall(){
        return service.getall();
    }

    @GetMapping("/{id}")
    public  Product getsingle(@PathVariable Long id){
        return service.getsingle(id);
    }

    @PutMapping("/{id}")
    public  Product update(@PathVariable Long id,@RequestParam String name, @RequestParam double price, @RequestParam String des, @RequestParam MultipartFile image){
        return service.updateproduct(id,name,price,des,image);
    }

    @DeleteMapping("/{id}")
    public String delete(@PathVariable Long id){
        return  service.delete(id);
    }
}

package com.example.productcrud.service;

import com.example.productcrud.model.Product;
import com.example.productcrud.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
@Service
public class ProductService {

    @Autowired
    private ProductRepository repo;

    @Value("${upload.path}")
    private String uploadpath;


    public Product addproduct(String name, double price, String des, MultipartFile file){

        try{
            String filename= file.getOriginalFilename();
            String uploadDir = System.getProperty("user.dir") + File.separator + uploadpath;

            Files.createDirectories(Paths.get(uploadDir));

            String filepath = uploadDir + File.separator + filename;
            File f=new File(filepath);
            file.transferTo(f);

            Product product=new Product();
            product.setName(name);
            product.setPrice(price);
            product.setDes(des);
            product.setImage(filename);
            return repo.save(product);

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public List<Product> getall(){
        return repo.findAll();
    }

    public Product getsingle(Long id){
        return repo.findById(id).orElseThrow();
    }

    public Product updateproduct(Long id,String name, double price, String des, MultipartFile file){
        Product p=getsingle(id);

        p.setName(name);
        p.setDes(des);
        p.setPrice(price);

        if((file!=null && !file.isEmpty())){
            try{

                String filename= file.getOriginalFilename();
                String uploadDir = System.getProperty("user.dir") + File.separator + uploadpath;
                String filepath = uploadDir + File.separator + filename;
                File f=new File(filepath);
                file.transferTo(f);
                p.setImage(filename);

            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        }
        return repo.save(p);
    }

    public String delete(Long id){
        repo.deleteById(id);
        return "Product deleted success";
    }
}

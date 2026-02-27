package com.example.productservlat;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.server.servlet.context.ServletComponentScan;

@SpringBootApplication
@ServletComponentScan
public class ProductservlatApplication {

	public static void main(String[] args) {
		SpringApplication.run(ProductservlatApplication.class, args);
	}

}

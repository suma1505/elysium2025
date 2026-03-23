package com.example.oauth2client.config;


import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.Customizer;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.web.SecurityFilterChain;

import java.net.http.HttpClient;

@Configuration
public class SecurityConfig {

    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {

        http
                .csrf(csrf->csrf.disable())
                .authorizeHttpRequests(request->request
                        .requestMatchers("/api/public").permitAll()
                        .anyRequest().authenticated()
                )
                .oauth2Client(Customizer.withDefaults());
        return http.build();
    }
}

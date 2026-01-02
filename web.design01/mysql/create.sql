show databases;

create database company;

use company;

select database();

create table students(
id int primary key auto_increment,
name varchar(50),
age int,
dept varchar(40));

show tables;

desc students;

drop table students;

drop database company;

create database school;

use school;

select database();

create table students(
id int primary key auto_increment,
name varchar(50),
age int,
dept varchar(40));

desc students;

insert into students (name,age,dept) values
("uma",21,"it"),
("aravinth",22,"it"),
("vicky",23,"it"),
("prarthana",24,"it");

select * from students;

select name,dept from students;

select * from students limit 3;

select name as sname ,dept as sdept from students;




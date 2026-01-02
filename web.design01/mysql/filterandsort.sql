create database school;

use school;

select database();

create table students(
id int primary key auto_increment,
name varchar(50),
age int,
dept varchar(40),
city varchar(60));

desc students;

insert into students (name,age,dept,city) 
values ("uma",21,"it","ariyalur"),
 ("aravinth",21,"finance","trichy"),
("vicky",23,"sotware developer","trichy"),
("prarthana",24,"it","ariyalur");

select * from students where dept ='it';

select * from students where age between 20 and 22;

select * from students  order by age desc;

select * from students order by dept asc, age desc;

select * from students limit 3;

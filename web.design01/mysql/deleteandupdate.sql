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

select * from students;

set sql_safe_updates = 0;

update students set dept ="it" where id =2;

update students set age = age +1;

update students set city ="chennai"  where dept ='it';

delete from students where age > 22;

delete from students where name ='vicky';

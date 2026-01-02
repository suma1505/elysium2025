create database college;

use college;

create table departments(
dept_id int primary key auto_increment,
dept_name varchar(50));

insert into departments (dept_name)
values
("computer science"),
("information technology"),
("finance"),
("human resources");

create table students(
s_id int primary key auto_increment,
name varchar(59),
dept_id int,
city varchar(50),
foreign key (dept_id) references departments(dept_id)
);

insert into students (name, dept_id, city)
values
('Rahul', 1, 'Chennai'),
('Priya', 2, 'Madurai'),
('Karthik', 3, 'Trichy'),
('Divya', 2, 'Salem'),
('Anand', NULL, 'Coimbatore');

select * from students;

select students.name,departments.dept_name from students 
inner join departments on 
students.dept_id = departments.dept_id;

select students.name,departments.dept_name from students 
left join departments on 
students.dept_id = departments.dept_id;

select students.name,departments.dept_name from students 
right join departments on 
students.dept_id = departments.dept_id;

select students.name,departments.dept_name from students 
left join departments on 
students.dept_id = departments.dept_id
union
select students.name,departments.dept_name from students 
right join departments on 
students.dept_id = departments.dept_id;

select students.name,departments.dept_name from students 
cross join departments;


create database student_management;

use student_management;

create table students(
student_id int auto_increment primary key,
student_name varchar(100) not null,
email varchar(100) unique,
age int,
city varchar(50)
);

create table courses(
course_id int auto_increment primary key,
course_name varchar(100) not null,
instructor varchar(100)
);

create table enrollments(
enrollment_id int auto_increment primary key,
student_id int,
course_id int,
enrollment_date DATE DEFAULT (CURRENT_DATE),
foreign key (student_id) references students(student_id) on delete cascade,
foreign key (course_id) references courses(course_id) on delete cascade
);

insert into students(student_name,email,age,city)values
('Alice','alice@gmail.com',20,'chennai'),
('Bob','bob@gmail.com',22,'coimbatore'),
('Charlie','charlie@gmail.com',21,'madurai');

insert into courses(course_name,instructor)values
('Database Systems', 'Dr.Ramesh'),
('Web Development', 'Mr.Priya'),
('Data Science', 'Mr.Raj');

insert into enrollments(student_id,course_id)values
(1,1),
(1,2),
(2,2),
(3,3);

insert into students(student_name,email,age,city)values
('David','david@gmail.com',23,'salem');

select * from students;

update students set city = 'Trichy' where student_id = 2;

delete from students where student_id = 3;

select s.student_name,c.course_name, c.instructor, e.enrollment_date
from enrollments e join students s on e.student_id = s.student_id
join courses c on e.course_id = c.course_id;
 
select s.student_name, c.course_name from students s left join 
enrollments e on e.student_id = s.student_id
left join courses c on e.course_id = c.course_id;

select s.student_name, count(e.course_id) as total_courses
from students s left join enrollments e on s.student_id = e.student_id
group by s.student_name;

select c.course_name, count(e.student_id) as total_students
from courses c left join enrollments e on c.course_id = e.course_id
group by c.course_name;



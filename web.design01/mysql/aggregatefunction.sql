create database company;

use company;

create table employees(
id int primary key auto_increment,
name varchar(50),
dept varchar(40),
salary float,
city varchar(60)
);


insert into employees (name, dept, salary, city) values
('Rahul', 'IT', 40000, 'Chennai'),
('Priya', 'HR', 35000, 'Madurai'),
('Karthik', 'Finance', 50000, 'Coimbatore'),
('Divya', 'IT', 45000, 'Salem'),
('Anand', 'Marketing', 30000, 'Trichy'),
('Ravi', 'IT', 48000, 'Erode'),
('Sneha', 'Finance', 52000, 'Chennai');

select count(*) as total_emp from employees;

select count(*) as total_it_emp from employees where dept = 'it';

select sum(salary) as total_sal from employees;

select sum(salary) as total_finance_sal from employees where dept = 'finance';

select avg(salary) as avg_sal from employees;

select avg(salary) as avg_it_emp from employees where dept = 'it';

select min(salary) as lowest_salary from employees;
select max(salary) as highest_salary from employees;

select max(salary) as finance_max
from employees
where dept = 'Finance';

select 
    count(*) as total_employees,
    sum(salary) as total_salary,
    avg(salary) as avg_salary,
    min(salary) as min_salary,
    max(salary) as max_salary
from employees;

select
    dept,
    count(*) as emp_count,
    avg(salary) as avg_salary,
    sum(salary) as total_salary
from employees
group by dept;

select 
    city,
    sum(salary) as total_city_salary,
    count(*) AS emp_count
from employees
group by city;

select count(*) as total_employees FROM employees;

select sum(salary) as total_company_salary FROM employees;

select avg(salary) as avg_it_salary
from employees
where dept = 'IT';

select
    min(salary) as min_finance_salary,
    max(salary) as max_finance_salary
from employees
where dept = 'Finance';

select
    dept,
    count(*) as emp_count,
    avg(salary) as avg_salary
from employees
group by dept;


select
    city,
    sum(salary) as total_salary,
    count(*) as employee_count
from employees
group by city;

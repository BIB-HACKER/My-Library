-- DCL (data control language)######################################

select * from mydbms.`employee` where emp_id=3;
select * from mydbms.`employee` where salary=150000;

select*from mydbms.`employee`;

-- SQL logical operator :-
select * from mydbms.`employee`where first_name='Bibhakar' and salary='150000';
select*from mydbms.`employee` where first_name='malay' or salary='50000';

select * from mydbms.`employee` where salary>30000;
select * from mydbms.`employee` where salary<50000;
select*from mydbms.`employee` where salary between 30000 and 50000;
select * from mydbms.`employee` where last_name like 'p%';
select*from mydbms.`employee` where salary in (100,30000,50000);
select distinct(first_name) from mydbms.`employee`;

-- SQL Operators - Aggregations Function / NUMERICAL Function
select max(salary) from mydbms.`employee`;
select min(salary) from mydbms.`employee`;
select avg(salary) from mydbms.`employee`;
select count(*) from mydbms.`employee`;

-- SQL GROPU BY Clause
update mydbms.`employee` set dept='Technology' where emp_id='1';
update mydbms.`employee` set dept='social marketing' where emp_id='5';
update mydbms.`employee` set dept='cleint handaling'where emp_id='6';

select first_name, max(salary),dept from mydbms.`employee` group by dept;
select first_name, max(salary),dept from mydbms.`employee` group by salary;

-- SQL HAVING Clause
select first_name, max(salary), dept from mydbms.`employee` group by dept having count(dept)>=2;
select avg(salary), dept from mydbms.`employee` group by dept having count(dept)>=2;

-- SQL ORDER BY Clause
select * from mydbms.`employee` order by salary desc;
select * from mydbms.`employee` order by salary asc;

-- SQL UNION
create table `mydbms`.`product1` (
catagory_id int,
product_name varchar(20),
primary key (`catagory_id`)
);

select * from mydbms.`product1`;

-- insert into mydbms.`product1`(`catagory_id`,`product_name`) values ('1','nokia');
update mydbms.product1 set catagory_id = 7 where product_name='nokia';
delete from mydbms.product1 where product_name in ('nokia');
insert into mydbms.`product1` values (1,'nokia');
delete from mydbms.product1 where product_name in ('python');
commit;
-- ###################################################
create table `mydbms`.`product2` (
catagory_id int,
product_name varchar(20),
primary key (`catagory_id`)
);
insert into mydbms.`product2` values('9','samsung');
select * from mydbms.`product2`;
delete from mydbms.product2 where product_name in ('samsung');

-- SQL UNION ALL 
select product_name from mydbms.`product1`
union all
select product_name from mydbms.`product2`;

-- SQL JOINS
create table mydbms.`depertment`(
dept_id int,
dept varchar(20),
dept_loc varchar(20)
);
insert into mydbms.`depertment` values (7,'Technology','UK');
-- update mydbms.depertment set dept_id=33 where dept='sales';
-- delete from mydbms.depertment where dept in('hr');
select * from mydbms.depertment;
-- SQL JOINS
select e.first_name,e.salary,d.dept,d.dept_loc
from mydbms.employee e
-- left join mydbms.depertment d
-- right join mydbms.depertment d
inner join mydbms.depertment d
on e.dept=d.dept;

-- SQL LEFT JOIN
select e.first_name,e.salary,d.dept,d.dept_loc
from mydbms.employee e
left join mydbms.depertment d
on e.dept=d.dept;
-- union
select e.first_name,e.salary,d.dept,d.dept_loc
from mydbms.employee e
right join mydbms.depertment d
on e.dept=d.dept;

-- SQL CROSS JOIN 
select * from mydbms.employee cross join mydbms.depertment;
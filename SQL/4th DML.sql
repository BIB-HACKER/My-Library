-- DML - data manipulation language
insert into mydbms.`employee`(`emp_id`,`first_name`,`last_name`,`salary`,`job_code`) values 
('3','malay','malakar','100','12');

update mydbms.`employee`set `emp_id` = '111' where emp_id = '1';

delete from mydbms.`employee`

select*from mydbms.`employee`;

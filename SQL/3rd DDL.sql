-- DDL-->(Data defination language) #############################################################

create table `mydbms`.`employee` (
    `emp_id` int not null,
    `first_name` varchar(20) not null,
    `last_name` varchar(20) not null,
    `salary` int not null,
    PRIMARY KEY (`emp_id`)
);

SELECT * FROM mydbms.`employee`;  -- TABLE GLANCE

describe mydbms.`employee`;

alter table mydbms.`employee` add column contact int;
alter table mydbms.`employee` add column contacts int;
alter table mydbms.`employee` add column dept varchar(20);
alter table mydbms.`employee` drop column contact;

alter table mydbms.`employee` rename column contact to job_code;            

truncate table mydbms.`employee`;

-- drop table mydbms.`employee`; 
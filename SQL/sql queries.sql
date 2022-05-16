create table `mydbms`.`cricket_2` (
Player_id varchar(20),
Player_name varchar(20),
Runs int,
Popularity int
);

select * from mydbms.`cricket_1`;
select * from mydbms.`cricket_2`;
insert into mydbms.`cricket_2` values ('PL7','Tutai',45,40);

select * from mydbms.`cricket_1`
union
select * from mydbms.`cricket_2`;

select Player_name from mydbms.`cricket_1`
union
select Player_name from mydbms.`cricket_2`;

select player_name, popularity from mydbms.cricket_1
where Popularity > (select avg(Popularity) from mydbms.`cricket_1`);
select avg(popularity) from mydbms.`cricket_1`;

select player_name,Player_id from mydbms.`cricket_1` where cricket_1.player_id in (select Player_id from mydbms.`cricket_2`);

select player_id,player_name,runs from mydbms.`cricket_1` where runs > (select avg(runs) from mydbms.`cricket_1`);
select avg(runs) from mydbms.`cricket_1`;

select * from mydbms.`cricket_1` where Player_name like 's%';
select * from mydbms.`cricket_2` where Player_name like 'b%';

select * from mydbms.`cricket_1` where Player_name not like '%t';

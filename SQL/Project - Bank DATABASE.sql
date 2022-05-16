create database BANK;
#########
use bank;
#################################
-- CREATE TABLE-->

create table bank.bank_details(
product char(10),
quantity int,
price real,
purchase_cost decimal(6,2),
estimated_sale_price float

);
--##################################### 
select*from bank.bank_details;
####################
describe bank.bank_details;
#######################
-- INSERT VLAUE IN TABLE-->
insert into bank.bank_details values ('paycard',3,200,8008,9009);
insert into bank.bank_details values ('paypoint',4,100,8000,6800);
##########################################
-- NEW COLUME ADD-->
alter table bank.bank_details add column geo_location varchar(20);
#########################################
select geo_location from bank.bank_details where product='paycard';
#########################################
select char_length(product) from bank.bank_details where product='paypoint';
select char_length(product) from bank.bank_details where product='paycard';
###########################################
-- MODIFIE(STRUCHAR CHANGE) PRODUCT TYPE FIELD-->
alter table bank.bank_details modify product varchar(10);
###########################################
-- CREATE NEW TABLE-->
create table bank.bank_holidays(
holiday date,
start_time time,               -- (Here - date,datetime,timestamp are a KEYWORD) 
end_time timestamp
);

describe bank.bank_holidays;
select *from bank.bank_holidays;
############################################

#INSERT values IN TABLE-->
insert into bank.bank_holidays values(
current_date(),
current_date(),
current_date()
);
##############################
#VALUE UOPDATE
update bank.bank_holidays set holiday = date_add(holiday,interval 1 day); #(here holiday colume interval -> 22-05-13 update to 22-05-14)
update bank.bank_holidays set holiday = date_add(holiday,interval -5 day); #(here holiday colume intrval -> 22-05-13 update to 22-05-08) 
select * from bank.bank_holidays;

# END TIME COLUME UPDATE TO EUROPEAN TIME-->
update bank.bank_holidays set end_time = utc_timestamp();  #(here end_time colume -> 00-00-00 time update to european time)
select * from bank.bank_holidays;

################################
#JUST DISPLAY BANK_DETAILS "HOLIDAY" COLUME SHOW "NEW_HOLIDAY" COLUME -->
select product as new_product from bank.bank_details;
select * from bank.bank_details;
####################################
# DISPLAY ONLY 1ST ROW IN TABLE -->
select * from bank.bank_details limit 1;
select * from bank.bank_holidays limit 1;




drop table cac;

create table cac
(
date date,
value float,
volume int,
name varchar(6),
Rendements float);

#'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\'
       
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/datacac.csv' 
INTO TABLE cac 
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\r\n'
Ignore 1 lines
(@date,value,volume,name,Rendements)
SET date = STR_TO_DATE(@date, '%d/%m/%Y');


select * from cac;
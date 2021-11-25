#drop table cac;

create table cac
(
Dates DATETIME,
Valeurs FLOAT,
Volumes int,
Noms varchar(6));


#LOAD DATA INFILE 'C:/Program Files/MySQL/MySQL Server 8.0/DonneesActifs.csv' 
#INTO TABLE cac 
#FIELDS TERMINATED BY ';' 
#ENCLOSED BY '"'
#LINES TERMINATED BY '\n';

select * from cac;

#drop table cac;

create table cac
(
Dates DATETIME,
Valeurs FLOAT,
Volumes int,
Noms varchar(6));


#LOAD DATA INFILE 'C:\Users\camil\Desktop\PI²\DonneesActifs.csv' 
#INTO TABLE cac 
#FIELDS TERMINATED BY ';' 
#ENCLOSED BY '"'
#LINES TERMINATED BY '\n';

select * from cac;
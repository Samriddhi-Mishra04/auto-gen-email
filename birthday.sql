create database birthday_db;
use birthday_db;
drop table users;
create table users( id int auto_increment primary key, name varchar(100) not null, email varchar(100) not null, birthday date not null);
insert into users (name, email, birthday) values ('John Doe', 'john@example.com', '1990-01-20'), ('Jane Smith', 'jane@example.com', '1995-01-25');
insert into users (name, email, birthday) values ('Sam', 'itsnoneofyourbusiness.7013@gmail.com', '2020-01-24');
SELECT user, host FROM mysql.user;
SHOW GRANTS FOR 'username'@'host';
SELECT User, Host, Db 
FROM mysql.db
WHERE Db = 'birthday_db';
select* from users;
SELECT name, email, birthday FROM users;
update users set birthday = "2025-01-29" where name = "Sam";

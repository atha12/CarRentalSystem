-- create database carRental;

-- use carRental;

-- create table roles(
--     role_id int auto_increment primary key,
--     type varchar(40) not null,
--     description varchar(255) not null
--     );

-- insert into roles (type,description) values ('customer','Customer for a car to rent.'),('admin','Administrator for a managing activities.'),('driver','A driver if required for the rented car.');

-- create table users(
--     id int(10) auto_increment primary key,
--     fname varchar(40) not null,
--     lname varchar(40) not null,
--     email varchar(40) not null,
--     contact varchar(10),
--     address varchar(255),
--     password varchar(40) not null,
--     role int(10),
--     foreign key(role) references roles(role_id),
--     debit int(20),
--     salary int(20),
--     workhr int(20)
--     );

-- insert into users (fname,lname,email,contact,address,password,role) values ('Atharva','Kamat','atharva.makarand15@gmail.com',9833567286,'502,Guruprasad Natwar Nagar','12345',2);

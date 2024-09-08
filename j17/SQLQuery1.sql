use python410
create table users(
	u_id int identity(1, 1),
	u_name nvarchar(300) not null,
	u_pid nchar(10),
	u_tel varchar(20),
	u_email nvarchar(30)
	primary key(u_id, u_pid)
);

INSERT INTO users (u_name, u_pid, u_tel, u_email)
VALUES
('Cardinal', '0025565341', '02177163338', 'asghar@jalalyan.ir'),
('Greasy Burger', '23456787', '234567898', 'Sandnes@gmail.com'),
('Tasty Tee', '345678954', '34567879654', 'Liverpool@yahoo.com');

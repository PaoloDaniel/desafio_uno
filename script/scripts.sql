--Aqui se encuentran todo los scripts para ejecutar en PostgreSQL--
--A pesar de que el enunciado decia que el codigo deberia estar en ingles--
--los escripts he hice tomando en cuenta las palabras del enunciado, para asi evitar malentendido al leer las tablas--


--Table Clientes

create table Clientes(
	rut int primary key,
	rut_v int not null, 
	nombre varchar(50) not null unique,
	razon_social varchar(20),
	fecha_inicio_firma Date
);

--Table Medidor
create table Medidor(
	ECOM_ID varchar(50) primary key,
	rut int not null,
	id_medidor varchar(20) not null unique,
	direccion varchar(50) not null,
	numero_instalacion int,
	FOREIGN KEY (rut) REFERENCES Clientes(rut)
);
--Function que se encarga de generar la id de ECOM_ID
create or replace function generator()
returns trigger as
$BODY$
begin
update Medidor
set ECOM_ID = concat(id_medidor, SUBSTRING((select nombre from Clientes where Medidor.rut=Clientes.rut),1,2))
where rut=(select rut from Clientes where Medidor.rut=Clientes.rut);
return new;
end;
$BODY$
language plpgsql;

--Trigger que se encarga de ejecutarse despues de insertar una nueva fila a Medidores
create trigger ECOM_ID_Generator 
after insert
on Medidor
execute procedure generator();


---Insert Ejemplos de Clientes
insert into Clientes (rut, rut_v, nombre, razon_social, fecha_inicio_firma) values(1111111,1,'Nueva Vida','Sociedad Colectiva','05/07/2016');
insert into Clientes (rut, rut_v, nombre, razon_social, fecha_inicio_firma) values(2222222,2,'Los Soles','Sociedad Cooperativa','11/03/2020');

---Insert Ejemplos de Medidores
insert into Medidor (ECOM_ID, rut, id_medidor, direccion, numero_instalacion) values('',1111111,'ABC123', 'Calle siempre viva 123', 1);
insert into Medidor (ECOM_ID, rut, id_medidor, direccion, numero_instalacion) values('',1111111,'ABC321', 'Calle siempre viva 111', 2);
insert into Medidor (ECOM_ID, rut, id_medidor, direccion, numero_instalacion) values('',2222222,'OLQ987', 'Vitacura 609', 3);
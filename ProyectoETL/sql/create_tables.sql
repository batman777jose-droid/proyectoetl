CREATE DATABASE ProyectoETL;
GO

USE ProyectoETL;
GO

CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100),
    ciudad VARCHAR(100),
    edad INT
);

CREATE TABLE Ventas (
    id_venta INT PRIMARY KEY,
    id_cliente INT,
    producto VARCHAR(100),
    cantidad INT,
    precio DECIMAL(10,2),
    fecha DATE
);

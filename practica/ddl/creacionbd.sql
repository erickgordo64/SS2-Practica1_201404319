-- Tabla Dimensión Clientes
CREATE TABLE DimCliente (
    ClienteID INT IDENTITY(1,1) PRIMARY KEY,
    NombreCliente VARCHAR(100),
    Direccion VARCHAR(200)
);

-- Tabla Dimensión Empleados
CREATE TABLE DimEmpleado (
    EmpleadoID INT IDENTITY(1,1) PRIMARY KEY,
    NombreEmpleado VARCHAR(100),
    PuestoEmpleado VARCHAR(50)
);

-- Tabla Dimensión Productos
CREATE TABLE DimProducto (
    ProductoID INT IDENTITY(1,1) PRIMARY KEY,
    NombreProducto VARCHAR(100),
    Descripcion VARCHAR(200),
    Peso float,
    PrecioProducto float
);

-- Tabla Dimensión Tiempo
CREATE TABLE DimTiempo (
    TiempoID INT IDENTITY(1,1) PRIMARY KEY,
    Dia VARCHAR(50),
    Mes VARCHAR(50),
    Anio INT
);

-- Tabla Dimensión Ciudad
CREATE TABLE DimCiudad (
    CiudadID INT IDENTITY(1,1) PRIMARY KEY,
    NombreCiudad VARCHAR(50)
);

-- Tabla de Hechos Entregas
CREATE TABLE HechosEntregas (
    EntregaID INT PRIMARY KEY,
    ClienteID INT REFERENCES DimCliente(ClienteID),
    EmpleadoID INT REFERENCES DimEmpleado(EmpleadoID),
    ProductoID INT REFERENCES DimProducto(ProductoID),
    TiempoID INT REFERENCES DimTiempo(TiempoID),
    CiudadID INT REFERENCES DimCiudad(CiudadID),
    EstadoEntrega VARCHAR(50),
    CostoEnvio float,
    TiempoEntrega INT
);


CREATE TABLE Entregas (
    EntregaID INT,
    Dia VARCHAR(50),
    Mes VARCHAR(50),
    Anio INT,
    NombreCliente VARCHAR(100),
    Direccion VARCHAR(200),
    NombreEmpleadoEntrega VARCHAR(100),
    PuestoEmpleadoEntrega VARCHAR(50),
    CiudadEntrega VARCHAR(50),
    NombreProducto VARCHAR(100),
    Descripcion VARCHAR(200),
    Peso float,
    TiempoEntrega INT,
    EstadoEntrega VARCHAR(50),
    CostoEnvio float,
    PrecioProducto float
);
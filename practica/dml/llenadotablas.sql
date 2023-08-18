-- insercion de registro en tabla DimCiudad
insert into DimCiudad(NombreCiudad) select distinct CiudadEntrega from Entregas;

-- insercion de registrtos en tabla DimCliente
insert into DimCliente(NombreCliente, Direccion) select distinct NombreCliente, Direccion from Entregas;

-- insercion de registros en tabla DimEmpleado
insert into DimEmpleado(NombreEmpleado, PuestoEmpleado) select distinct NombreEmpleadoEntrega, PuestoEmpleadoEntrega from Entregas;

-- insercion de registro en tabla DimProductos
insert into DimProducto(NombreProducto, Descripcion, Peso, PrecioProducto) select distinct NombreProducto, Descripcion, Peso, PrecioProducto from Entregas;

-- insercion de registros en tabla DimTiempo
insert into DimTiempo(Dia, Mes, Anio) select distinct Dia, Mes, Anio from Entregas;

-- insercion de registro en hechos entregas
insert into HechosEntregas select ent.EntregaId, cl.ClienteID, emp.EmpleadoID, pro.ProductoID, tim.TiempoID, ciu.CiudadID, ent.EstadoEntrega, ent.CostoEnvio, ent.TiempoEntrega from Entregas ent
inner join DimCliente cl on cl.NombreCliente = ent.NombreCliente and cl.Direccion = ent.Direccion
inner join DimEmpleado emp on emp.NombreEmpleado = ent.NombreEmpleadoEntrega
inner join DimProducto pro on pro.NombreProducto = ent.NombreProducto and pro.Peso = ent.Peso and pro.PrecioProducto = ent.PrecioProducto
inner join DimTiempo tim on tim.Anio = ent.Anio and tim.Dia = ent.Dia and tim.Mes = ent.Mes
inner join DimCiudad ciu on ciu.NombreCiudad = ent.CiudadEntrega
order by ent.EntregaID;
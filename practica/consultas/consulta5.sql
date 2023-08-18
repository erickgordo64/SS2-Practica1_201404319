select top 5 count(pro.NombreProducto) as c, pro.NombreProducto ,he.EstadoEntrega from HechosEntregas he
inner join DimProducto pro on pro.ProductoID = he.ProductoID
where he.EstadoEntrega = 'Pendiente'
group by pro.NombreProducto, he.EstadoEntrega order by c desc;
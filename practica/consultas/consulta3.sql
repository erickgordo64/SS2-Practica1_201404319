-- consulta 3
select top 5 he.CostoEnvio, pro.NombreProducto from HechosEntregas he
inner join DimProducto pro on pro.ProductoID = he.ProductoID
order by he.CostoEnvio desc;
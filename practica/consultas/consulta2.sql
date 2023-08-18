-- consulta 2
select top 5 count(NombreCliente) as t, NombreCliente from DimCliente group by NombreCliente order by t desc;
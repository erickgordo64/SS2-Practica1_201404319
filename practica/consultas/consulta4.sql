-- consulta 4
select top 5 count(he.CiudadID) as c, ciu.NombreCiudad from DimCiudad ciu
inner join HechosEntregas he on he.CiudadID = ciu.CiudadID
group by he.CiudadID, ciu.NombreCiudad order by c desc;
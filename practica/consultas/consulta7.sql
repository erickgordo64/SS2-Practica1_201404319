-- consulta 7
select count(he.CiudadID), ciu.NombreCiudad from HechosEntregas he
inner join DimCiudad ciu on ciu.CiudadID = he.CiudadID
group by ciu.NombreCiudad;
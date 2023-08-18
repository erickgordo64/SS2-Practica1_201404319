-- consulta 10
select COUNT(tie.Anio) as entregas, tie.Anio from DimTiempo tie
inner join HechosEntregas he on he.TiempoID = tie.TiempoID
group by tie.Anio;
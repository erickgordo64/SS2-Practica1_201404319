-- consulta 8
select COUNT(tie.Dia) as entregas, tie.Dia from DimTiempo tie
inner join HechosEntregas he on he.TiempoID = tie.TiempoID
group by tie.Dia;
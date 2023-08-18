-- consulta 9
select COUNT(tie.mes) as entregas, tie.mes from DimTiempo tie
inner join HechosEntregas he on he.TiempoID = tie.TiempoID
group by tie.mes;
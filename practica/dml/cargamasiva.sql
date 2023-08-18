BULK INSERT Entregas
FROM 'C:\Users\erick\Documents\GitHub\SS2-Practica1_201404319\practica\dml\entregas.csv'
WITH (
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2 -- Si tu archivo tiene una fila de encabezado
);
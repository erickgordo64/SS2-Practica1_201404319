WITH cte AS (
    SELECT EntregaID, ROW_NUMBER() OVER (
            PARTITION BY
                EntregaID
            ORDER BY
                EntregaID
        ) row_num
     FROM
        Entregas
)
DELETE FROM cte
WHERE row_num > 1;

-- Eliminar registros con celdas vacías en el año
DELETE FROM Entregas
WHERE Anio IS NULL OR Anio = '';

-- Eliminar registros con NombreProducto vacío
DELETE FROM Entregas
WHERE NombreProducto IS NULL OR LTRIM(RTRIM(NombreProducto)) = '';

-- Eliminar registros con EstadoEntrega vacío
DELETE FROM Entregas
WHERE EstadoEntrega IS NULL OR LTRIM(RTRIM(EstadoEntrega)) = '';

-- Eliminar registros con PrecioProducto vacío
DELETE FROM Entregas
WHERE PrecioProducto IS NULL;
SELECT
    c.ID_Compra,
    p.Nome_Produto,
    c.Quantidade,
    p.Preco_Unitario,
    (c.Quantidade * p.Preco_Unitario) AS Valor_Total
FROM Compras c
INNER JOIN Produtos p
    ON c.ID_Produto = p.ID_Produto;

SELECT
    p.ID_Produto,
    p.Nome_Produto,
    SUM(c.Quantidade) AS Quantidade_Total
FROM Produtos p
INNER JOIN Compras c
    ON p.ID_Produto = c.ID_Produto
GROUP BY
    p.ID_Produto,
    p.Nome_Produto
ORDER BY Quantidade_Total DESC
LIMIT 1;

SELECT
    p.ID_Produto,
    p.Nome_Produto,
    COALESCE(SUM(c.Quantidade), 0) AS Quantidade_Total
FROM Produtos p
LEFT JOIN Compras c
    ON p.ID_Produto = c.ID_Produto
GROUP BY
    p.ID_Produto,
    p.Nome_Produto;
WITH Fibonacci (id, prev_number, number) AS
(
     SELECT 0,
	 CAST(0 AS FLOAT), 
	 CAST(1 AS FLOAT)
     UNION ALL
     SELECT id + 1, number, prev_number + number
     FROM Fibonacci
     WHERE id < 90
)
SELECT id AS FibonacciID, 
     prev_number
     FROM Fibonacci;
GO
SELECT people.id, people.name, COUNT(sales.id) as sale_count, SUM(sales.price) as sale_rank FROM sbertest.dbo.people AS people

LEFT JOIN sbertest.dbo.sales 
ON people.id = sales.people_id
GROUP BY people.id, people.name
ORDER BY sale_count DESC;
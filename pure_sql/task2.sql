SELECT
PARSENAME(REPLACE(people.name, ' ', '.'), 2) AS Имя,
PARSENAME(REPLACE(people.name, ' ', '.'), 3) AS Фамилия,
PARSENAME(REPLACE(people.name, ' ', '.'), 1) AS Отчество

FROM sbertest.dbo.task_2 as people
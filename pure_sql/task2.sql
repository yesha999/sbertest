SELECT
PARSENAME(REPLACE(people.name, ' ', '.'), 2) AS ���,
PARSENAME(REPLACE(people.name, ' ', '.'), 3) AS �������,
PARSENAME(REPLACE(people.name, ' ', '.'), 1) AS ��������

FROM sbertest.dbo.task_2 as people
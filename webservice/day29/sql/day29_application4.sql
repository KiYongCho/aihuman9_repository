SELECT id, company, position, salary
FROM jobs
WHERE location = %s
ORDER BY salary DESC
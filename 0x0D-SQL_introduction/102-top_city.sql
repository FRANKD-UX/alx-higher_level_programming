-- Get the top 3 hottest cities in July and August, ordered by average temperature
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8) -- July (7) and August (8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;


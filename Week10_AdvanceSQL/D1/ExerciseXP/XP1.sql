-- Task 1
SELECT m.medal_name, AVG(gc.age) AS avg_age
FROM games_competitor gc
JOIN medal m ON gc.id = m.id
WHERE m.medal_name IN ('Gold', 'Silver', 'Bronze')
GROUP BY m.medal_name;

--Task 2
SELECT nr.region_name, COUNT(DISTINCT p.id) AS unique_competitors
FROM person p
JOIN person_region pr ON p.id = pr.person_id
JOIN noc_region nr ON pr.region_id = nr.id
WHERE p.id IN (
    SELECT ce.competitor_id
    FROM competitor_event ce
    GROUP BY ce.competitor_id
    HAVING COUNT(DISTINCT ce.event_id) > 3
)
GROUP BY nr.region_name
ORDER BY unique_competitors DESC
LIMIT 5;


--Task 3
WITH medal_count AS (
    SELECT ce.competitor_id, COUNT(ce.medal_id) AS total_medals
    FROM competitor_event ce
    JOIN medal m ON ce.medal_id = m.id
    WHERE m.medal_name IN ('Gold', 'Silver', 'Bronze')
    GROUP BY ce.competitor_id
)
CREATE TEMPORARY TABLE competitor_medals AS
SELECT competitor_id, total_medals
FROM medal_count
WHERE total_medals > 2;



--Task 4
CREATE TEMPORARY TABLE competitor_analysis AS
SELECT competitor_id, full_name
FROM person;

DELETE FROM competitor_analysis
WHERE competitor_id NOT IN (
    SELECT ce.competitor_id
    FROM competitor_event ce
    JOIN medal m ON ce.medal_id = m.id
    WHERE m.medal_name IN ('Gold', 'Silver', 'Bronze')
);

-- Task 1
CREATE TEMPORARY TABLE competitors_both_seasons_medals AS
WITH season_medals AS (
    SELECT ce.competitor_id, e.season, COUNT(m.id) AS total_medals
    FROM competitor_event ce
    JOIN event e ON ce.event_id = e.id
    JOIN medal m ON ce.medal_id = m.id
    WHERE m.medal_name IN ('Gold', 'Silver', 'Bronze')
    GROUP BY ce.competitor_id, e.season
)
SELECT competitor_id,
       SUM(CASE WHEN season = 'Summer' THEN total_medals ELSE 0 END) AS summer_medals,
       SUM(CASE WHEN season = 'Winter' THEN total_medals ELSE 0 END) AS winter_medals
FROM season_medals
GROUP BY competitor_id
HAVING SUM(CASE WHEN season = 'Summer' THEN 1 ELSE 0 END) > 0
   AND SUM(CASE WHEN season = 'Winter' THEN 1 ELSE 0 END) > 0;

SELECT * FROM competitors_both_seasons_medals;

-- Task 2
CREATE TEMPORARY TABLE competitors_two_sports_medals AS
SELECT ce.competitor_id, COUNT(DISTINCT e.sport_id) AS distinct_sports, COUNT(medal_id) AS total_medals
FROM competitor_event ce
JOIN event e ON ce.event_id = e.id
WHERE ce.medal_id IS NOT NULL
GROUP BY ce.competitor_id
HAVING COUNT(DISTINCT e.sport_id) = 2;

SELECT competitor_id, total_medals
FROM competitors_two_sports_medals
ORDER BY total_medals DESC
LIMIT 3;

-- Task 3
WITH competitor_event_medals AS (
    SELECT ce.competitor_id, ce.event_id, COUNT(ce.medal_id) AS total_medals
    FROM competitor_event ce
    WHERE ce.medal_id IS NOT NULL
    GROUP BY ce.competitor_id, ce.event_id
),
max_event_medals AS (
    SELECT competitor_id, MAX(total_medals) AS max_medals
    FROM competitor_event_medals
    GROUP BY competitor_id
)

SELECT nr.region_name, SUM(mem.max_medals) AS total_medals
FROM max_event_medals mem
JOIN person_region pr ON mem.competitor_id = pr.person_id
JOIN noc_region nr ON pr.region_id = nr.id
GROUP BY nr.region_name
ORDER BY total_medals DESC
LIMIT 5;


-- Task 4
CREATE TEMPORARY TABLE competitors_no_medals AS
SELECT p.id AS competitor_id, p.full_name, COUNT(DISTINCT ce.games_id) AS num_games
FROM person p
JOIN competitor_event ce ON p.id = ce.competitor_id
LEFT JOIN medal m ON ce.medal_id = m.id
WHERE ce.medal_id IS NULL
GROUP BY p.id, p.full_name
HAVING COUNT(DISTINCT ce.games_id) > 3;
SELECT * FROM competitors_no_medals;

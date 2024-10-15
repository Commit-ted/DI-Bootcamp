-- Task 1
UPDATE person p
SET height = (
    SELECT AVG(p2.height)
    FROM person p2
    JOIN person_region pr ON p2.id = pr.person_id
    JOIN person_region pr2 ON p.id = pr2.person_id
    WHERE pr.region_id = pr2.region_id
    AND p2.height > 0  -- Assuming heights of 0 are missing data and should be excluded
)
WHERE height = 0;  -- Update only those rows where height is missing

-- Task 2
CREATE TEMPORARY TABLE multi_event_competitors (
    competitor_id INTEGER,
    games_id INTEGER,
    total_events INTEGER
);

INSERT INTO multi_event_competitors (competitor_id, games_id, total_events)
SELECT competitor_id, games_id, total_events
FROM (
    SELECT ce.competitor_id, ce.games_id, COUNT(ce.event_id) AS total_events
    FROM competitor_event ce
    GROUP BY ce.competitor_id, ce.games_id
    HAVING COUNT(ce.event_id) > 1
) AS filtered_events;


-- Task 3

SELECT nr.region_name
FROM noc_region nr
JOIN person_region pr ON nr.id = pr.region_id
JOIN competitor_event ce ON pr.person_id = ce.competitor_id
JOIN medal m ON ce.medal_id = m.id
WHERE m.medal_name IN ('Gold', 'Silver', 'Bronze')
GROUP BY nr.region_name
HAVING AVG(
    SELECT COUNT(med.medal_id) 
    FROM competitor_event




-- Task 4
CREATE TEMPORARY TABLE competitor_season_participation AS
SELECT competitor_id, season
FROM competitor_event ce
JOIN event e ON ce.event_id = e.id
GROUP BY competitor_id, season;

CREATE TEMPORARY TABLE both_seasons_competitors AS
SELECT competitor_id
FROM competitor_season_participation
GROUP BY competitor_id
HAVING COUNT(DISTINCT season) = 2;

--1
SELECT 
    g.genre_name,
    m.title,
    RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS popularity_rank
FROM 
    movie m
    JOIN movie_genres mg ON m.movie_id = mg.movie_id
    JOIN genre g ON mg.genre_id = g.genre_id
ORDER BY 
    g.genre_name,
    popularity_rank; 

--2
SELECT 
    g.genre_name,
    m.title,
    m.revenue,
    NTILE(4) OVER (PARTITION BY g.genre_name ORDER BY m.revenue DESC) AS revenue_quartile
FROM 
    movie m
    JOIN movie_genres mg ON m.movie_id = mg.movie_id
    JOIN genre g ON mg.genre_id = g.genre_id
WHERE 
    m.revenue IS NOT NULL
ORDER BY 
    g.genre_name,
    revenue_quartile;

--3
SELECT 
    g.genre_name,
    m.title,
    m.budget,
    SUM(m.budget) OVER (PARTITION BY g.genre_name ORDER BY m.title ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total_budget
FROM 
    movie m
    JOIN movie_genres mg ON m.movie_id = mg.movie_id
    JOIN genre g ON mg.genre_id = g.genre_id
ORDER BY 
    g.genre_name,
    m.title;

--4
SELECT 
    g.genre_name,
    FIRST_VALUE(m.title) OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS most_recent_movie,
    FIRST_VALUE(m.release_date) OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS release_date
FROM 
    movie m
    JOIN movie_genres mg ON m.movie_id = mg.movie_id
    JOIN genre g ON mg.genre_id = g.genre_id
GROUP BY 
    g.genre_name
ORDER BY 
    g.genre_name;

--5
SELECT 
    p.person_name AS actor_name,
    DENSE_RANK() OVER (ORDER BY COUNT(mc.movie_id) DESC) AS appearance_rank
FROM 
    movie_cast mc
    JOIN person p ON mc.person_id = p.person_id
GROUP BY 
    p.person_name
ORDER BY 
    appearance_rank;
--6
WITH DirectorRatings AS (
    SELECT 
        p.person_name AS director_name,
        AVG(m.vote_average) AS average_rating
    FROM 
        movie m
        JOIN movie_crew mc ON m.movie_id = mc.movie_id
        JOIN person p ON mc.person_id = p.person_id
        JOIN department d ON mc.department_id = d.department_id
    WHERE 
        d.department_name = 'Directing'
    GROUP BY 
        p.person_name
)
SELECT 
    director_name,
    average_rating
FROM 
    DirectorRatings
ORDER BY 
    average_rating DESC
LIMIT 10;

--7
SELECT 
    p.person_name AS actor_name,
    SUM(m.revenue) OVER (PARTITION BY p.person_name) AS cumulative_revenue
FROM 
    movie m
    JOIN movie_cast mc ON m.movie_id = mc.movie_id
    JOIN person p ON mc.person_id = p.person_id
ORDER BY 
    cumulative_revenue DESC;

--8
WITH DirectorBudgets AS (
    SELECT 
        p.person_name AS director_name,
        SUM(m.budget) AS total_budget
    FROM 
        movie m
        JOIN movie_crew mc ON m.movie_id = mc.movie_id
        JOIN person p ON mc.person_id = p.person_id
        JOIN department d ON mc.department_id = d.department_id
    WHERE 
        d.department_name = 'Directing'
    GROUP BY 
        p.person_name
)
SELECT 
    director_name,
    total_budget
FROM 
    DirectorBudgets
ORDER BY 
    total_budget DESC
LIMIT 10;


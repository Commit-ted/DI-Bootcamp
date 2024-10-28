--1
WITH BudgetGrowth AS (
    SELECT 
        pc.company_name,
        m.movie_id,
        m.budget,
        LAG(m.budget) OVER (PARTITION BY pc.company_name ORDER BY m.release_date) AS previous_budget
    FROM 
        movie m
        JOIN movie_company mc ON m.movie_id = mc.movie_id
        JOIN production_company pc ON mc.company_id = pc.company_id
)
SELECT 
    company_name,
    AVG((budget - previous_budget) * 1.0 / NULLIF(previous_budget, 0)) AS avg_budget_growth_rate
FROM 
    BudgetGrowth
WHERE 
    previous_budget IS NOT NULL
GROUP BY 
    company_name;

--2
WITH AverageRating AS (
    SELECT 
        AVG(vote_average) AS overall_avg_rating
    FROM 
        movie
),
HighRatedActors AS (
    SELECT 
        p.person_name AS actor_name,
        COUNT(m.movie_id) AS high_rated_movies_count
    FROM 
        movie m
        JOIN movie_cast mc ON m.movie_id = mc.movie_id
        JOIN person p ON mc.person_id = p.person_id,
        AverageRating ar
    WHERE 
        m.vote_average > ar.overall_avg_rating
    GROUP BY 
        p.person_name
)
SELECT 
    actor_name,
    high_rated_movies_count
FROM 
    HighRatedActors
ORDER BY 
    high_rated_movies_count DESC
LIMIT 10;



--3
WITH GenreRevenue AS (
    SELECT 
        g.genre_name,
        m.title,
        m.revenue,
        m.release_date
    FROM 
        movie m
        JOIN movie_genres mg ON m.movie_id = mg.movie_id
        JOIN genre g ON mg.genre_id = g.genre_id
)
SELECT 
    genre_name,
    title,
    revenue,
    AVG(revenue) OVER (
        PARTITION BY genre_name 
        ORDER BY release_date 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_avg_revenue
FROM 
    GenreRevenue
ORDER BY 
    genre_name, release_date;




--4
WITH SeriesRevenue AS (
    SELECT 
        k.keyword_name AS series_name,
        SUM(m.revenue) AS total_series_revenue
    FROM 
        movie m
        JOIN movie_keywords mk ON m.movie_id = mk.movie_id
        JOIN keyword k ON mk.keyword_id = k.keyword_id
    GROUP BY 
        k.keyword_name
)
SELECT 
    series_name,
    total_series_revenue
FROM 
    SeriesRevenue
ORDER BY 
    total_series_revenue DESC
LIMIT 10;

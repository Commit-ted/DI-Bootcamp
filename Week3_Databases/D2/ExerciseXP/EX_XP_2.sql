
-- EX_XP 2 dvdrental

--1
-- SELECT * FROM customer;

--2
-- SELECT first_name || ' ' || last_name AS full_name FROM customer;
--3
-- SELECT DISTINCT create_date FROM customer;
-- SELECT create_date FROM customer
--4
-- SELECT * FROM customer ORDER BY first_name DESC;
-- SELECT * FROM customer ORDER BY first_name ASC;
--5
-- SELECT film_id, title, description, release_year, rental_rate
-- FROM film
-- ORDER BY rental_rate ASC;
-- SELECT film_id, title, description, release_year, rental_rate
-- FROM film
-- ORDER BY rental_rate DESC;
--6
-- SELECT address, phone 
-- FROM address 
-- WHERE district = 'Texas';

--7
-- SELECT * FROM film WHERE film_id IN (15, 150);

--8
-- SELECT * FROM film
-- SELECT film_id, title, description, length, rental_rate
-- FROM film
-- WHERE title = 'Tequila Past';

--9
-- SELECT film_id, title, description, length, rental_rate
-- FROM film
-- WHERE title LIKE 'Ma%';

--10
-- SELECT * FROM film ORDER BY rental_rate ASC LIMIT 10;


--11 --- NEEED--A
-- SELECT * FROM film ORDER BY rental_rate ASC OFFSET 10 LIMIT 10;
--11  --B
-- SELECT *
-- FROM film
-- ORDER BY rental_rate ASC
-- OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY;
--11  --C
-- WITH RankedMovies AS (
--     SELECT *,
--            ROW_NUMBER() OVER (ORDER BY rental_rate ASC) AS row_num
--     FROM film
-- )

-- SELECT *
-- FROM RankedMovies
-- WHERE row_num > 10 AND row_num <= 20
-- ORDER BY rental_rate ASC;

--12
-- SELECT c.first_name, c.last_name, p.amount, p.payment_date
-- FROM customer c
-- JOIN payment p ON c.customer_id = p.customer_id
-- ORDER BY c.customer_id ASC;


--13
-- SELECT f.*
-- FROM film f
-- LEFT JOIN inventory i ON f.film_id = i.film_id
-- WHERE i.film_id IS NULL;


--14
-- SELECT city.city, country.country 
-- FROM city 
-- JOIN country ON city.country_id = country.country_id;


--15
SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, p.staff_id
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY p.staff_id ASC;


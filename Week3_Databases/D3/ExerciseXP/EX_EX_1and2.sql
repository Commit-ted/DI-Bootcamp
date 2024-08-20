--EX-XP 1
--1
-- SELECT * FROM language;
--2
-- SELECT f.title, f.description, l.name AS language_name
-- FROM film f
-- JOIN language l ON f.language_id = l.language_id;
--3
-- SELECT f.title, f.description, l.name AS language_name
-- FROM language l
-- LEFT JOIN film f ON l.language_id = f.language_id;
--4
-- --Create the new_film table
-- CREATE TABLE new_film (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL
-- );

-- -- Add some new films to the table
-- INSERT INTO new_film (name) VALUES
-- ('New Film 1'),
-- ('New Film 2'),
-- ('New Film 3');
-- Check
-- SELECT * from new_film

--5
-- Create the customer_review table
-- CREATE TABLE customer_review (
--     review_id SERIAL PRIMARY KEY,
--     film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
--     language_id INT REFERENCES language(language_id),
--     title VARCHAR(255) NOT NULL,
--     score INT CHECK (score BETWEEN 1 AND 10),
--     review_text TEXT,
--     last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );
--6 
-- Add movie reviews
-- INSERT INTO customer_review (film_id, language_id, title, score, review_text)
-- VALUES 
-- ((SELECT id FROM new_film WHERE name = 'New Film 1'), 
--  (SELECT language_id FROM language WHERE name = 'English'), 
--  'Great Movie!', 8, 'I really enjoyed this movie. It was thrilling and well-paced.'),

-- ((SELECT id FROM new_film WHERE name = 'New Film 2'), 
--  (SELECT language_id FROM language WHERE name = 'Spanish'), 
--  'Not Bad', 6, 'The movie was okay, but it could have been better in terms of story.');
--7
-- Delete a film from the new_film table
-- DELETE FROM new_film WHERE name = 'New Film 1';

-- -- Check if the corresponding review has been deleted
-- SELECT * FROM customer_review;


--EX-XP 2

-- 1
-- Example: Change the language of films with title 'New Film 1' to 'French'
-- UPDATE film
-- SET language_id = (SELECT language_id FROM language WHERE name = 'French')
-- WHERE title = 'New Film 1';
--2
-- SELECT * FROM customer
--Foreign keys: customer, store_id, addres_id, city_id
-- How this affects INSERT:
-- Referential Integrity: When inserting a new row into the customer table, you must ensure that the store_id and address_id values already exist in their respective tables (store, address).
-- Valid Foreign Keys: You cannot insert a customer with an address_id or store_id that doesn't exist in the referenced tables, or it will violate the foreign key constraint.

--3
-- Drop the customer_review table
-- DROP TABLE customer_review;

--4
-- SELECT COUNT(*)
-- FROM rental
-- WHERE return_date IS NULL;

-- 5
-- SELECT f.title, f.rental_rate
-- FROM rental r
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- WHERE r.return_date IS NULL
-- ORDER BY f.rental_rate DESC
-- LIMIT 30;

--6
--6.1
-- SELECT f.title
-- FROM film f
-- JOIN film_actor fa ON f.film_id = fa.film_id
-- JOIN actor a ON fa.actor_id = a.actor_id
-- WHERE a.first_name = 'Penelope' AND a.last_name = 'Monroe'
-- AND (f.description LIKE '%sumo%' OR f.title LIKE '%sumo%');

--6.2
-- SELECT title
-- FROM film
-- WHERE length < 60 AND rating = 'R';

--6.3
-- SELECT f.title
-- FROM rental r
-- JOIN payment p ON r.rental_id = p.rental_id
-- JOIN customer c ON r.customer_id = c.customer_id
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
-- AND p.amount > 4.00
-- AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

--6.4
-- SELECT f.title
-- FROM rental r
-- JOIN customer c ON r.customer_id = c.customer_id
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
-- AND (f.title LIKE '%boat%' OR f.description LIKE '%boat%')
-- ORDER BY f.replacement_cost DESC
-- LIMIT 1;

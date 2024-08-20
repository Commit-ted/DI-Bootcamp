-- PARENT TABLE
-- CREATE TABLE colors(
-- color_id SERIAL PRIMARY KEY,
-- color_name VARCHAR(50)
-- )

-- INSERT INTO colors (color_name) VALUES
-- ('Red'), ('Blue'), ('Green'), ('Yellow');
-- SELECT * FROM colors

-- -- CHILD TABLE: DELETE / UPDATE
-- CREATE TABLE car_restrict(
-- cars_id SERIAL PRIMARY KEY, car_name VARCHAR(50),
-- car_color_id INTEGER REFERENCES colors (color_id) ON DELETE RESTRICT
-- )

-- INSERT INTO car_restrict (car_name, car_color_id) VALUES
-- ('Toyota', 1),
-- ('Ford', 2),
-- ('Fonda', 3),
-- ('Mazda', 1)

-- SELECT * FROM car_restrict

-- DELETE FROM colors
-- WHERE color_id = 2 --error 

-- INSERT INTO colors (color_name) VALUES
-- ('Purple');

-- SELECT * FROM colors

-- -- Cascadde
-- CREATE TABLE car_cascade(
-- cars_id SERIAL PRIMARY KEY, car_name VARCHAR(50),
-- car_color_id INTEGER REFERENCES colors (color_id) ON DELETE CASCADE
-- )

-- INSERT INTO car_cascade (car_name, car_color_id) VALUES
-- ('Toyota', 1),
-- ('Ford', 2),
-- ('Fonda', 3),
-- ('Mazda', 1)


-- DELETE FROM colors WHERE color_id = 2

-- SELECT * FROM colors

-- EX-Class
-- CREATE TABLE car_set_default(
-- cars_id SERIAL PRIMARY KEY, 
-- car_name VARCHAR(50),
-- car_color INTEGER DEFAULT 1 REFERENCES colors (color_id) ON DELETE SET DEFAULT
-- )

-- ALTER TABLE car_set_default RENAME COLUMN car_color TO car_color_id;

-- INSERT INTO car_set_default (car_name, car_color_id) VALUES
-- ('Toyota', 1),
-- ('Ford', 2),
-- ('Fonda', 3),
-- ('Mazda', 1)

UPDATE car_set_default
SET car_color_id = 4
WHERE car_name = 'Ford';

SELECT * FROM car_set_default
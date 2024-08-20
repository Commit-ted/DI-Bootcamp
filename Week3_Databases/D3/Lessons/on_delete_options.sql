-- PARENT TABLE

-- CREATE TABLE colors(
-- color_id SERIAL PRIMARY KEY,
-- color_name VARCHAR(50)
-- )

-- INSERT INTO colors (color_name) VALUES 
-- ('Red'),('Blue'), ('Green'), ('Yellow')

-- SELECT * FROM colors

-- CHILD TABLE: OPTIONS FOR DELETE/UPDATE
-- OPTION 1: RESTRICT

-- CREATE TABLE cars_restrict(
-- car_id SERIAL PRIMARY KEY,car_name VARCHAR(50),
-- car_color_id INTEGER REFERENCES colors (color_id) ON DELETE RESTRICT
-- )

-- INSERT INTO cars_restrict (car_name, car_color_id) VALUES
-- ('Toyota',1),
-- ('Ford', 2),
-- ('Honda', 3),
-- ('Mazda', 2)

-- select * from cars_restrict

-- DELETE FROM colors 
-- WHERE color_id = 2 --error (cant delete because this column is "on restrict")

-- INSERT INTO colors (color_name) VALUES 
-- ('Purple')

-- DELETE FROM colors 
-- WHERE color_id = 5

-- select * from colors

-- UPDATE colors
-- SET color_id = 10
-- WHERE color_id = 1; -- error: because color_id is on delete restrict

-- select * from colors

-- OPTION 2: CASCADE

-- CREATE TABLE cars_cascade 
-- (car_id SERIAL PRIMARY KEY,
--  car_name VARCHAR(50),
-- car_color_id INTEGER REFERENCES colors (color_id) ON DELETE CASCADE
-- )

-- INSERT INTO cars_set_default (car_name, car_color_id) VALUES
-- ('Toyota',1),
-- ('Ford', 2),
-- ('Honda', 3),
-- ('Mazda', 2)

-- DELETE FROM colors WHERE color_id = 2 -- Allows to delete and deletes the whole row from the child
-- select * from cars_cascade

-- EXERCISE IN CLASS:

-- 1 - Create a table called cars_set_default. It will have three columns: 
-- car_id (the primary key), car_name and car_color (CAR COLOR WILL BE SET DEFAULT): 
-- car_color INTEGER DEFAULT 1 REFERENCES colors (color_id) ON DELETE SET DEFAULT ON UPDATE SET DEFAULT
-- INSERT data to the cars_set_default table:

-- INSERT INTO cars_cascade (car_name, car_color_id) VALUES
-- ('Toyota',1),
-- ('Ford', 2),
-- ('Honda', 3),
-- ('Mazda', 2)

-- 2 - create a delete statement to delete from the colors table one color id.

-- 3 - select * from cars_set_default and analyse. What happened?

-- CREATE TABLE cars_set_default (
-- car_id SERIAL PRIMARY KEY,
-- car_name VARCHAR(50),
-- car_color INTEGER DEFAULT 1 REFERENCES colors (color_id) ON DELETE SET DEFAULT ON UPDATE SET DEFAULT)

-- SELECT * FROM cars_set_default
-- SELECT * FROM colors

-- INSERT INTO cars_set_default (car_name, car_color_id) VALUES
-- ('Toyota',1),
-- ('Ford', 4),
-- ('Honda', 3),
-- ('Mazda', 1)

-- SELECT * FROM cars_set_default

-- DELETE FROM colors where color_id = 4;
-- SELECT * FROM cars_set_default


-- # PAY ATTENTION:  
-- - IF YOU HAVE A CHAIN (EX.: PARENT, CHILD, GRANDCHILD) AND ONE OF THE TABLES (CHILD OR GRANDCHILD) IS "RESTRICT" THE CHANGE WILL NOT BE APPLIED FOR THE WHOLE CHAIN

-- ## 3- OTHER POSSIBILITIES:
-- - NO ACTION
-- - SET NULL
-- - SET DEFAULT

-- ## DIFFERENCE BETWEEN NO ACTION AND RESTRICT:
-- Practical Implication: In most cases, the effect of using NO ACTION or RESTRICT will be the same. However, in complex scenarios involving deferred constraints, NO ACTION may allow other operations to proceed before enforcing the referential integrity, whereas RESTRICT enforces it immediately.



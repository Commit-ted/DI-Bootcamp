-- Part I

-- Create the Customer table
CREATE TABLE Customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

-- Create the Customer_profile table with a one-to-one relationship
CREATE TABLE Customer_profile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT false,
    customer_id INTEGER UNIQUE REFERENCES Customer(id)
);

-- Insert customers
INSERT INTO Customer (first_name, last_name) VALUES
('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive');

-- Insert customer profiles using subqueries
INSERT INTO Customer_profile (isLoggedIn, customer_id)
VALUES
(true, (SELECT id FROM Customer WHERE first_name='John' AND last_name='Doe')),
(false, (SELECT id FROM Customer WHERE first_name='Jerome' AND last_name='Lalu'));

-- 1. Display the first_name of the LoggedIn customers
SELECT c.first_name
FROM Customer c
JOIN Customer_profile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = true;

-- 2. Display all customers' first_name and isLoggedIn status, including those without a profile
SELECT c.first_name, cp.isLoggedIn
FROM Customer c
LEFT JOIN Customer_profile cp ON c.id = cp.customer_id;

-- 3. Count the number of customers that are not LoggedIn
SELECT COUNT(*)
FROM Customer c
LEFT JOIN Customer_profile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = false OR cp.isLoggedIn IS NULL;

-- Part II

-- Create the Book table
CREATE TABLE Book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL
);

-- Insert books
INSERT INTO Book (title, author) VALUES
('Alice In Wonderland', 'Lewis Carroll'),
('Harry Potter', 'J.K Rowling'),
('To Kill a Mockingbird', 'Harper Lee');

-- Create the Student table with a CHECK constraint on age
CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    age INTEGER CHECK (age <= 15)
);

-- Insert students
INSERT INTO Student (name, age) VALUES
('John', 12),
('Lera', 11),
('Patrick', 10),
('Bob', 14);

-- Create the Library junction table for Many-to-Many relationship
CREATE TABLE Library (
    book_fk_id INTEGER REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
    student_fk_id INTEGER REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id)
);

-- Insert records into the Library table using subqueries
INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES
(
    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM Student WHERE name = 'John'),
    '2022-02-15'
),
(
    (SELECT book_id FROM Book WHERE title = 'To Kill a Mockingbird'),
    (SELECT student_id FROM Student WHERE name = 'Bob'),
    '2021-03-03'
),
(
    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM Student WHERE name = 'Lera'),
    '2021-05-23'
),
(
    (SELECT book_id FROM Book WHERE title = 'Harry Potter'),
    (SELECT student_id FROM Student WHERE name = 'Bob'),
    '2021-08-12'
);

-- Display all columns from the Library table
SELECT * FROM Library;

-- Select the name of the student and the title of the borrowed books
SELECT s.name, b.title
FROM Library l
JOIN Student s ON l.student_fk_id = s.student_id
JOIN Book b ON l.book_fk_id = b.book_id;

-- Select the average age of the children who borrowed 'Alice In Wonderland'
SELECT AVG(s.age) AS average_age
FROM Library l
JOIN Student s ON l.student_fk_id = s.student_id
JOIN Book b ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice In Wonderland';

-- Delete a student from the Student table
DELETE FROM Student WHERE name = 'Bob';

-- Verify what happened in the Library table
SELECT * FROM Library;

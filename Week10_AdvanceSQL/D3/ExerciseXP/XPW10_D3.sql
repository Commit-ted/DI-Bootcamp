--
CREATE TABLE emp_dataset AS
SELECT *
FROM salaries
LEFT JOIN companies
ON salaries.comp_name = companies.company_name
LEFT JOIN functions
ON salaries.func_code = functions.function_code
LEFT JOIN employees
ON salaries.employee_id = employees.employee_code_emp; 



-- 2
CREATE TABLE df_employee AS
SELECT 
    employee_id || '_' || CAST(date AS TEXT) AS id,  -- Use || for concatenation and CAST date to TEXT
    DATE(date) AS month_year,  -- Use DATE() function to cast the timestamp to a DATE format
    employee_id, 
    employee_name, 
    `GEN(M_F)` AS gender,  -- Rename the column to "gender"
    age,
    salary,
    function_group, 
    company_name, 
    company_city, 
    company_state, 
    company_type, 
    const_site_category
FROM emp_dataset;
--
SELECT * FROM df_employee;
--

UPDATE df_employee
SET
    id = TRIM(id),
    employee_name = TRIM(employee_name),
    gender = TRIM(gender),
    function_group = TRIM(function_group),
    company_name = TRIM(company_name),
    company_city = TRIM(company_city),
    company_state = TRIM(company_state),
    company_type = TRIM(company_type),
    const_site_category = TRIM(const_site_category);

--

SELECT *
FROM df_employee
WHERE id IS NULL
   OR month_year IS NULL
   OR employee_id IS NULL
   OR employee_name IS NULL
   OR gender IS NULL
   OR age IS NULL
   OR salary IS NULL
   OR function_group IS NULL
   OR company_name IS NULL
   OR company_city IS NULL
   OR company_state IS NULL
   OR company_type IS NULL
   OR const_site_category IS NULL;
--
DELETE FROM df_employee
WHERE const_site_category = ''


--3

SELECT company_name, COUNT(employee_id) AS employee_count
FROM df_employee
GROUP BY company_name; 

--4
WITH city_totals AS (
    SELECT company_city, COUNT(employee_id) AS employee_count
    FROM df_employee
    GROUP BY company_city
),
city_percentages AS (
    SELECT company_city, employee_count, (employee_count * 100.0 / (SELECT SUM(employee_count) FROM city_totals)) AS percentage
    FROM city_totals
)
SELECT * FROM city_percentages;
-- TIME
UPDATE df_employee
SET month_year = SUBSTR(id, INSTR(id, '_') + 1);
--
SELECT month_year, COUNT(employee_id) AS employee_count
FROM df_employee
GROUP BY month_year;

-- Step 3: Calculate the average number of employees per month.
SELECT AVG(employee_count) AS avg_employees_per_month
FROM (
    SELECT month_year, COUNT(employee_id) AS employee_count
    FROM df_employee
    GROUP BY month_year
) monthly_counts;





--5

WITH monthly_counts AS (
    SELECT month_year, COUNT(employee_id) AS employee_count
    FROM df_employee
    GROUP BY month_year
)
SELECT month_year, employee_count
FROM monthly_counts
WHERE employee_count = (SELECT MIN(employee_count) FROM monthly_counts)
   OR employee_count = (SELECT MAX(employee_count) FROM monthly_counts);
--
SELECT month_year, function_group, AVG(employee_count) AS avg_employees
FROM (
    SELECT month_year, function_group, COUNT(employee_id) AS employee_count
    FROM df_employee
    GROUP BY month_year, function_group
) monthly_function_counts
GROUP BY month_year, function_group;

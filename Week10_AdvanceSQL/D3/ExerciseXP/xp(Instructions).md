# XP Exercises 

## What you will learn
- Techniques for data cleaning and transformation using SQL
- Methods to handle and preprocess data for analysis
- Steps to ensure data quality and consistency

## What you will create
- A cleaned and transformed dataset ready for analysis
- SQL scripts to automate data cleaning tasks

## Dataset
You will be using this [dataset](https://github.com/danmarques-dt/SQL_data_cleaning_and_analysis_employees/blob/main/companies.csv) for the following exercises. Please download all of the .csv files : company.csv, employees.csv, functions.csv, and salaries.csv.

Before starting your exercises, to work with this dataset, we will have to upload it in SQLiteOnline. As we did for the previous days, go to https://sqliteonline.com/ > Import > select all of the .csv files. Then a window of import the file should appear, change from "New-Auto" to "First Line" in Column Name on all of them, and if needed, change the delimiter from "," to ";". You have a preview, make sure the cells are well delimited then hit "ok".
You are ready to start !

---

## Exercise 1: Building a Comprehensive Dataset for Employee Analysis

1. Create a temporary table that join all tables and create a new one using LEFT JOIN.
2. Create an unique identifier code between the columns 'employee_id' and 'date' and call it 'id'.
3. Convert the column 'date' to DATE type because it was previously configured as TIMESTAMP.
4. Transform this new table into a dataset "df_employee" for analysis.

Hint : 
```sql
CREATE TABLE df_employee AS
SELECT 
    employee_id || '_' || CAST(date AS TEXT) AS id,  -- Use || for concatenation and CAST date to TEXT
    DATE(date) AS month_year,  -- Use DATE() function to cast the timestamp to a DATE format
    employee_id, 
    ..., 
    `...` AS gender,  
    ...,
    ...,
    ..., 
    ..., 
    ..., 
    ..., 
    ..., 
    ...
FROM emp_dataset;
```

You should get a new df-employee table with the following columns : id, month_year, employee_id, employee_name, gender, age, salary, function_group, company_name, company_city, company_state, company_type, and const_site_category. 

---

## Exercise 2: Cleaning Data for Consistency and Quality

1. run the following SQLite request and observe your new table.
   ```sql
   SELECT * FROM df_employee;
   ```
2. Remove all unwanted spaces from all text columns using TRIM
   Hint :
   ```sql
   UPDATE df_employee
   SET
   id = TRIM(id),
   ...
   ...;
   ```
   
3. Check for NULL values and empty values.
   Hint :
   ```sql
   SELECT *
   FROM df_employee
   WHERE id IS NULL
   OR month_year IS NULL
   OR employee_id IS NULL
   ...
   ....;
   ```

4. Delete rows of the detected missing values.
   Hint :
   ```sql
   DELETE FROM df_employee
   WHERE salary = ' '
   ;


---

## Exercise 3 : Calculating Current Employee Counts by Company

- How many employees do the companies have today?
- Group them by company
     
---

## Exercise 4 : Analyzing Employee Distribution by City and Over Time

- What is the total number of employees each city? Add a percentage column
- What is the total number of employees each month?
- What is the average number of employees each month?

---

## Exercise 5 : Analyzing Employment Trends and Salary Metrics

- What is the minimum and maximum number of employees throughout all the months? In which months were they?
- What is the monthly average number of employees by function group?
- What is the annual average salary?


---


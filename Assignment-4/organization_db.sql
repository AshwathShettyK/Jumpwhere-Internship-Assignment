-- Create the database
CREATE DATABASE organization_db;
USE organization_db;

-- Create dept table
CREATE TABLE dept(
deptno INT PRIMARY KEY,
dname VARCHAR(50) NOT NULL,
loc VARCHAR(50) NOT NULL
);

-- Create emp table
CREATE TABLE emp(
empno INT PRIMARY KEY,
ename VARCHAR(50) NOT NULL,
sal DECIMAL(10,2),
hire_date DATE,
commission DECIMAL(10,2),
deptno INT,
mgr INT,

FOREIGN KEY (deptno)
REFERENCES dept(deptno)
);

-- Insert values into dept table
INSERT INTO dept (deptno, dname, loc)
VALUES
(10, 'Accounts', 'Bangalore'),
(20, 'IT', 'Delhi'),
(30, 'Production', 'Chennai'),
(40, 'Sales', 'Hyd'),
(50, 'Admn', 'London');

-- Insert values into emp table
INSERT INTO emp
(empno, ename, sal, hire_date, commission, deptno, mgr)
VALUES
(1001, 'Sachin', 19000, '1980-01-01', 2100, 20, 1003),
(1002, 'Kapil', 15000, '1970-01-01', 2300, 10, 1003),
(1003, 'Stefen', 12000, '1990-01-01', 500,  20, 1007),
(1004, 'Williams', 9000, '2001-01-01', NULL, 30, 1007),
(1005, 'John', 5000, '2005-01-01', NULL, 30, 1006),
(1006, 'Dravid', 19000, '1985-01-01', 2400, 10, 1007),
(1007, 'Martin', 21000, '2000-01-01', 1040, NULL, NULL);

-- Select employee details of dept number 10 or 30
SELECT *
FROM emp
WHERE deptno IN (10,30);

-- Write a query to fetch all the dept details with more than 1 Employee.
SELECT d.deptno,
       d.dname,
       d.loc,
       COUNT(e.empno) AS emp_count
FROM dept d
JOIN emp e
ON e.deptno = d.deptno
GROUP BY d.deptno, d.dname, d.loc
HAVING COUNT(e.empno) > 1;

-- Write a query to fetch employee details whose name starts with the letter “S”
SELECT *
FROM emp
WHERE ename LIKE 'S%';

-- Select Emp Details Whose experience is more than 2 years
SELECT *
FROM emp
WHERE TIMESTAMPDIFF(
      YEAR,
      hire_date,
      CURDATE()
) > 2;

-- Write a SELECT statement to replace the char “a” with “#” in Employee Name ( Ex:  Sachin as S#chin)
SELECT ename,
       REPLACE(ename, 'a', '#') AS modified_name
FROM emp;

-- Write a query to fetch employee name and his/her manager name. 
SELECT e.ename AS Employee_Name,
       m.ename AS Manager_Name
FROM emp e
JOIN emp m
ON e.mgr = m.empno;

-- Fetch Dept Name , Total Salry of the Dept
SELECT d.dname,
       SUM(e.sal) AS Total_Salary
FROM dept d
JOIN emp e
ON d.deptno = e.deptno
GROUP BY d.dname;

-- Write a query to fetch ALL the  employee details along with department name, department location, irrespective of employee existance in the department.
SELECT e.*,
       d.dname,
       d.loc
FROM emp e
LEFT JOIN dept d
ON e.deptno = d.deptno;

-- Write an update statement to increase the employee salary by 10 %
UPDATE emp
SET sal = sal * 1.10
WHERE empno IS NOT NULL;

-- Write a statement to delete employees belong to Chennai location.
DELETE FROM emp
WHERE deptno IN (
    SELECT deptno
    FROM dept
    WHERE loc = 'Chennai'
);


-- Get Employee Name and gross salary (sal + comission) .
SELECT ename,
       sal + IFNULL(commission, 0) AS Gross_Salary
FROM emp;


-- Increase the data length of the column Ename of Emp table from 100 to 250 using ALTER statement
ALTER TABLE emp
MODIFY ename VARCHAR(250);


-- Write query to get current datetime
SELECT NOW();


-- Write a statement to create STUDENT table, with related 5 columns
CREATE TABLE student (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    course VARCHAR(50),
    age INT,
    city VARCHAR(50)
);


-- Write a query to fetch number of employees who are getting salary more than 10000
SELECT COUNT(*) AS Employee_Count
FROM emp
WHERE sal > 10000;


-- Write a query to fetch minimum salary, maximum salary and average salary from emp table.
SELECT MIN(sal) AS Min_Salary,
       MAX(sal) AS Max_Salary,
       AVG(sal) AS Avg_Salary
FROM emp;


-- Write a query to fetch number of employees in each location
SELECT d.loc,
       COUNT(e.empno) AS Employee_Count
FROM dept d
LEFT JOIN emp e
ON d.deptno = e.deptno
GROUP BY d.loc;


-- Write a query to display employee names in descending order
SELECT ename
FROM emp
ORDER BY ename DESC;


-- Write a statement to create a new table (EMP_BKP) from the existing EMP table
CREATE TABLE emp_bkp AS
SELECT *
FROM emp;


-- Write a query to fetch first 3 characters from employee name appended with salary.
SELECT CONCAT(SUBSTRING(ename, 1, 3), sal) AS Name_Salary
FROM emp;


-- Get the details of the employees whose name starts with S
SELECT *
FROM emp
WHERE ename LIKE 'S%';


-- Get the details of the employees who work in Bangalore location
SELECT e.*
FROM emp e
JOIN dept d
ON e.deptno = d.deptno
WHERE d.loc = 'Bangalore';


-- Write the query to get the employee details whose name started within any letter between A and K
SELECT *
FROM emp
WHERE ename REGEXP '^[A-K]';


-- Write a query in SQL to display the employees whose manager name is Stefen
SELECT e.*
FROM emp e
JOIN emp m
ON e.mgr = m.empno
WHERE m.ename = 'Stefen';


-- Write a query in SQL to list the name of the managers who is having maximum number of employees working under him
SELECT m.ename
FROM emp e
JOIN emp m
ON e.mgr = m.empno
GROUP BY m.empno, m.ename
ORDER BY COUNT(*) DESC
LIMIT 1;


-- Write a query to display the employee details, department details and the manager details of the employee who has second highest salary
SELECT e.*,
       d.*,
       m.*
FROM emp e
LEFT JOIN dept d
ON e.deptno = d.deptno
LEFT JOIN emp m
ON e.mgr = m.empno
WHERE e.sal = (
    SELECT MAX(sal)
    FROM emp
    WHERE sal < (
        SELECT MAX(sal)
        FROM emp
    )
);

-- Write a query to list all details of all the managers
SELECT DISTINCT m.*
FROM emp e
JOIN emp m
ON e.mgr = m.empno;


-- Write a query to list the details and total experience of all the managers
SELECT DISTINCT m.*,
       TIMESTAMPDIFF(YEAR, m.hire_date, CURDATE()) AS Experience_Years
FROM emp e
JOIN emp m
ON e.mgr = m.empno;


-- Write a query to list the employees who is manager and takes commission less than 1000 and works in Delhi
SELECT DISTINCT m.*
FROM emp e
JOIN emp m
ON e.mgr = m.empno
JOIN dept d
ON m.deptno = d.deptno
WHERE IFNULL(m.commission, 0) < 1000
  AND d.loc = 'Delhi';


-- Write a query to display the details of employees who are senior to Martin
SELECT *
FROM emp
WHERE hire_date < (
    SELECT hire_date
    FROM emp
    WHERE ename = 'Martin'
);
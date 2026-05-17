-- ================================================
-- HR Analytics SQL Analysis
-- Dataset: IBM HR Analytics Employee Attrition
-- Author: Mohan R | Data Analyst
-- ================================================

-- 1. Total number of employees
SELECT COUNT(*) AS Total_Employees
FROM hr_data;

-- 2. Total attrition count and overall attrition rate
SELECT 
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition_Count,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Attrition_Rate_Percent
FROM hr_data;

-- 3. Attrition count and rate by Department
SELECT 
    Department,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition_Count,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Attrition_Rate_Percent
FROM hr_data
GROUP BY Department
ORDER BY Attrition_Rate_Percent DESC;

-- 4. Attrition by Job Role
SELECT 
    JobRole,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition_Count,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Attrition_Rate_Percent
FROM hr_data
GROUP BY JobRole
ORDER BY Attrition_Count DESC;

-- 5. Average Monthly Income by Department
SELECT 
    Department,
    ROUND(AVG(MonthlyIncome), 2) AS Avg_Monthly_Income
FROM hr_data
GROUP BY Department
ORDER BY Avg_Monthly_Income DESC;

-- 6. Average Monthly Income: Attrition Yes vs No
SELECT 
    Attrition,
    ROUND(AVG(MonthlyIncome), 2) AS Avg_Monthly_Income,
    ROUND(AVG(YearsAtCompany), 2) AS Avg_Years_At_Company
FROM hr_data
GROUP BY Attrition;

-- 7. Attrition by Age Group
SELECT 
    CASE 
        WHEN Age BETWEEN 18 AND 25 THEN '18-25'
        WHEN Age BETWEEN 26 AND 35 THEN '26-35'
        WHEN Age BETWEEN 36 AND 45 THEN '36-45'
        WHEN Age BETWEEN 46 AND 55 THEN '46-55'
        ELSE '55+'
    END AS Age_Group,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition_Count,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Attrition_Rate_Percent
FROM hr_data
GROUP BY Age_Group
ORDER BY Age_Group;

-- 8. Attrition by Gender
SELECT 
    Gender,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition_Count,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Attrition_Rate_Percent
FROM hr_data
GROUP BY Gender;

-- 9. Top 10 highest paid employees who left
SELECT 
    EmployeeNumber,
    JobRole,
    Department,
    MonthlyIncome,
    YearsAtCompany
FROM hr_data
WHERE Attrition = 'Yes'
ORDER BY MonthlyIncome DESC
LIMIT 10;

-- 10. Job Satisfaction vs Attrition
SELECT 
    JobSatisfaction,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition_Count,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Attrition_Rate_Percent
FROM hr_data
GROUP BY JobSatisfaction
ORDER BY JobSatisfaction;

-- 11. Employees with less than 2 years at company - attrition risk
SELECT 
    COUNT(*) AS High_Risk_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition_Count
FROM hr_data
WHERE YearsAtCompany < 2;

-- 12. Education Field distribution
SELECT 
    EducationField,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Attrition_Count
FROM hr_data
GROUP BY EducationField
ORDER BY Total_Employees DESC;

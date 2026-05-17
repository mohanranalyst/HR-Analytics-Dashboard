# HR Analytics Dashboard
**Tools Used:** Power BI | SQL | Python (Pandas, Matplotlib) | Excel

---

## Business Problem
A mid-sized company wanted to understand why employees were leaving and which departments had the highest attrition. HR leadership needed a clear, visual dashboard to monitor headcount, attrition rate, salary distribution, and employee demographics — to make faster and better workforce decisions.

---

## Dataset
- **Source:** IBM HR Analytics Employee Attrition Dataset (Kaggle)
- **Size:** 1,470 rows | 35 columns
- **Key Fields:** Age, Department, JobRole, MonthlyIncome, Attrition, YearsAtCompany, EducationField, Gender, JobSatisfaction, PerformanceRating

---

## What I Did

### 1. SQL Analysis
- Extracted and filtered employee records by department, role, and attrition status
- Calculated attrition count and rate per department using GROUP BY and aggregate functions
- Identified top salary bands and compared them with attrition patterns
- Ranked job roles by average monthly income

### 2. Python EDA
- Loaded and cleaned the dataset using Pandas
- Visualized attrition distribution by Department, Age Group, and Job Role using Matplotlib and Seaborn
- Calculated correlation between Monthly Income and Attrition
- Created Age Group buckets (18-25, 26-35, 36-45, 46-55, 55+) for segmented analysis

### 3. Power BI Dashboard
- Built 5 KPI cards: Total Employees, Attrition Count, Attrition Rate %, Avg Monthly Salary, Avg Years at Company
- Created bar charts: Attrition by Department, Attrition by Job Role, Attrition by Age Group
- Added pie chart: Employees by Education Field
- Added slicers: Department, Gender, Age Group
- Applied clean corporate color theme with consistent formatting

---

## Key Insights
- Overall attrition rate: **16.1%** (237 out of 1,470 employees left)
- **Sales department** had the highest attrition rate at over 20%
- Employees aged **26-35** had the highest attrition count
- **Laboratory Technicians** and **Sales Executives** were the most affected job roles
- Employees with **lower monthly income** showed significantly higher attrition
- Employees with **less than 2 years** at the company were most likely to leave

---

## Project Files

| File | Description |
|------|-------------|
| `HR_SQL_Analysis.sql` | SQL queries for attrition and salary analysis |
| `HR_Python_EDA.ipynb` | Python notebook with EDA charts and insights |
| `HR_Dashboard.png` | Power BI dashboard screenshot |

---

## Skills Demonstrated
- Data cleaning and transformation
- SQL aggregation and filtering
- Python EDA with Pandas and Matplotlib
- Power BI dashboard design with DAX measures
- KPI card creation and slicer-based interactivity
- Business insight generation from HR data

---

## Tools & Technologies
`Power BI` `SQL` `Python` `Pandas` `Matplotlib` `Seaborn` `Excel`

---

## Contact
- **Upwork:** https://www.upwork.com/freelancers/~01f1a46bcf0726b395
- **GitHub:** https://github.com/mohanranalyst
- **Location:** Pondicherry, India | Available 12 hours/day

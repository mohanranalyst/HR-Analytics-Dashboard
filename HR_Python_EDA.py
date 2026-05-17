# ================================================
# HR Analytics - Python EDA
# Dataset: IBM HR Analytics Employee Attrition
# Author: Mohan R | Data Analyst
# ================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ---- Load Dataset ----
df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')

print('Dataset Shape:', df.shape)
print('\nColumns:', df.columns.tolist())
print('\nFirst 5 rows:')
print(df.head())

# ---- Basic Info ----
print('\nDataset Info:')
print(df.info())

print('\nMissing Values:')
print(df.isnull().sum())

print('\nAttrition Value Counts:')
print(df['Attrition'].value_counts())

# ---- KPI Calculations ----
total_employees = len(df)
attrition_count = df[df['Attrition'] == 'Yes'].shape[0]
attrition_rate = round(attrition_count / total_employees * 100, 2)
avg_salary = round(df['MonthlyIncome'].mean(), 2)
avg_years = round(df['YearsAtCompany'].mean(), 2)

print(f'\n--- KEY METRICS ---')
print(f'Total Employees     : {total_employees}')
print(f'Attrition Count     : {attrition_count}')
print(f'Attrition Rate      : {attrition_rate}%')
print(f'Avg Monthly Income  : ${avg_salary}')
print(f'Avg Years at Company: {avg_years}')

# ---- Age Group Column ----
bins = [18, 25, 35, 45, 55, 100]
labels = ['18-25', '26-35', '36-45', '46-55', '55+']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=True)

# ---- Plot 1: Attrition by Department ----
plt.figure(figsize=(8, 5))
attrition_dept = df[df['Attrition'] == 'Yes']['Department'].value_counts()
sns.barplot(x=attrition_dept.index, y=attrition_dept.values, palette='Blues_d')
plt.title('Attrition Count by Department', fontsize=14, fontweight='bold')
plt.xlabel('Department')
plt.ylabel('Attrition Count')
plt.tight_layout()
plt.savefig('attrition_by_department.png')
plt.show()
print('Chart 1 saved: attrition_by_department.png')

# ---- Plot 2: Attrition by Age Group ----
plt.figure(figsize=(8, 5))
attrition_age = df[df['Attrition'] == 'Yes']['AgeGroup'].value_counts().sort_index()
sns.barplot(x=attrition_age.index, y=attrition_age.values, palette='Oranges_d')
plt.title('Attrition Count by Age Group', fontsize=14, fontweight='bold')
plt.xlabel('Age Group')
plt.ylabel('Attrition Count')
plt.tight_layout()
plt.savefig('attrition_by_age_group.png')
plt.show()
print('Chart 2 saved: attrition_by_age_group.png')

# ---- Plot 3: Attrition by Job Role ----
plt.figure(figsize=(10, 6))
attrition_role = df[df['Attrition'] == 'Yes']['JobRole'].value_counts()
sns.barplot(x=attrition_role.values, y=attrition_role.index, palette='Reds_d')
plt.title('Attrition Count by Job Role', fontsize=14, fontweight='bold')
plt.xlabel('Attrition Count')
plt.ylabel('Job Role')
plt.tight_layout()
plt.savefig('attrition_by_jobrole.png')
plt.show()
print('Chart 3 saved: attrition_by_jobrole.png')

# ---- Plot 4: Monthly Income - Attrition vs No Attrition ----
plt.figure(figsize=(7, 5))
sns.boxplot(x='Attrition', y='MonthlyIncome', data=df, palette='Set2')
plt.title('Monthly Income vs Attrition', fontsize=14, fontweight='bold')
plt.xlabel('Attrition')
plt.ylabel('Monthly Income ($)')
plt.tight_layout()
plt.savefig('income_vs_attrition.png')
plt.show()
print('Chart 4 saved: income_vs_attrition.png')

# ---- Plot 5: Attrition by Gender ----
plt.figure(figsize=(6, 5))
attrition_gender = df[df['Attrition'] == 'Yes']['Gender'].value_counts()
plt.pie(attrition_gender.values, labels=attrition_gender.index,
        autopct='%1.1f%%', colors=['#4C72B0', '#DD8452'])
plt.title('Attrition by Gender', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('attrition_by_gender.png')
plt.show()
print('Chart 5 saved: attrition_by_gender.png')

# ---- Plot 6: Education Field Distribution ----
plt.figure(figsize=(8, 5))
edu_dist = df['EducationField'].value_counts()
sns.barplot(x=edu_dist.values, y=edu_dist.index, palette='Purples_d')
plt.title('Employees by Education Field', fontsize=14, fontweight='bold')
plt.xlabel('Count')
plt.ylabel('Education Field')
plt.tight_layout()
plt.savefig('education_field.png')
plt.show()
print('Chart 6 saved: education_field.png')

# ---- Key Insights Summary ----
print('\n--- KEY INSIGHTS ---')
print(f'1. Overall Attrition Rate: {attrition_rate}%')
print(f'2. Highest Attrition Dept: {attrition_dept.idxmax()} ({attrition_dept.max()} employees)')
print(f'3. Most Affected Age Group: {attrition_age.idxmax()}')
print(f'4. Most Affected Job Role: {attrition_role.idxmax()}')
print(f'5. Avg Salary (Left): ${round(df[df["Attrition"]=="Yes"]["MonthlyIncome"].mean(),2)}')
print(f'6. Avg Salary (Stayed): ${round(df[df["Attrition"]=="No"]["MonthlyIncome"].mean(),2)}')
print('\nAnalysis Complete!')

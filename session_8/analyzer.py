import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('jobs_500.csv')

# 1 Job Titles ?
# job_titles = df['title'].value_counts()
# print(job_titles)

# plt.figure()
# job_titles.head(5).plot(kind="bar")
# plt.title("Job Titles in the Market")
# plt.xlabel("Job Roles")
# plt.ylabel("Job Counts")
# plt.xticks(rotation=45)
# plt.show()



# 2 Top Companies
# company_jobs = df['company'].value_counts()
# plt.figure()
# plt.title("Top Companies")
# company_jobs.plot(kind="bar")
# plt.show()


# 3 Locations
# company_jobs = df['location'].value_counts()
# plt.figure()
# plt.title("Top Locations")
# company_jobs.plot(kind="bar")
# plt.show()


# 4. Top Job Titles by Salary ?
# df['salary'] = df['salary'].astype(int)
# sorted_salary = df.sort_values(by="salary", ascending=False)
# print(sorted_salary.head(10)[['title', 'salary']])
# plt.figure()
# plt.bar(sorted_salary['title'], sorted_salary['salary'], color="red")
# plt.title("Top Job Titles by Salary")
# plt.show()

# 5. Location with Highest Average Salaries
# df_copy = df.copy()
# df_copy['salary'] = df_copy['salary'].astype(int)
# df_copy['salary'] = df_copy['salary'].apply(lambda x: round(x / 100000, 2))
# loc_salary = df_copy.groupby('location')['salary'].mean().sort_values(ascending=False)
# plt.figure()
# plt.bar(loc_salary.index, loc_salary.values, color="green")
# plt.ylabel("Salary in LPA(INR)")
# plt.title("Top Locations with Highest Average Salary")
# plt.show()


# 6. Job Titles with Highest salaries ?
# df_copy = df.copy()
# df_copy['salary'] = df_copy['salary'].astype(int)
# df_copy['salary'] = df_copy['salary'].apply(lambda x: round(x / 100000, 2))
# loc_salary = df_copy.groupby('title')['salary'].mean().sort_values(ascending=False)
# plt.figure()
# plt.bar(loc_salary.index, loc_salary.values, color="green")
# plt.ylabel("Salary in LPA(INR)")
# plt.xticks(rotation=35)
# plt.title("Top Job Titles with Highest Average Salary")
# plt.show()


# 7. Top Skills in Demand?
# skill_series = df["skills"].dropna().str.lower().str.split(", ")
# all_skills = sum(skill_series, [])
# skills_count = pd.Series(all_skills).value_counts()
# print(skills_count)
# Plot a chart


# 8. Top Paying Skills ?
# df_exploded = df.assign(skills=df['skills'].str.split(','))
# df_exploded['salary'] = df_exploded['salary'].apply(lambda x: round(x / 100000, 2))
# df_exploded = df_exploded.explode('skills')
# df_exploded = df_exploded.groupby("skills")['salary'].mean().sort_values(ascending=False)
# plt.figure()
# df_exploded.plot(kind="bar")
# plt.title("Top Paying Skills")
# plt.show()

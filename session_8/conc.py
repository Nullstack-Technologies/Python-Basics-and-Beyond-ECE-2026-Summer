import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('jobs_500.csv')
df["salary"] = df["salary"].astype(int)


#  Job Titles ?
# title_counts = df["title"].value_counts().head(10)

# plt.figure()
# title_counts.plot(kind="bar")
# plt.title("Most In-Demand Job Roles")
# plt.xlabel("Job Role")
# plt.ylabel("Count")
# plt.xticks(rotation=45)
# plt.show()


# Top Companies
# company_counts = df["company"].value_counts().head(10)
# plt.figure()
# company_counts.plot(kind="bar")
# plt.title("Top Hiring Companies")
# plt.xticks(rotation=45)
# plt.show()



# Top Locations
# location_counts = df["location"].value_counts()

# plt.figure()
# location_counts.plot(kind="bar")
# plt.title("Jobs by Location")
# plt.xticks(rotation=45)
# plt.show()



# Salary
# df["salary"] = df["salary"].astype(int)
# top_jobs = df.sort_values(by="salary", ascending=False)
# plt.figure()
# plt.bar(top_jobs['title'], top_jobs['salary'], color='skyblue')
# plt.title("Top 10 Salaries")
# plt.show()


# Location with Highest Salaries
# df_copy = df.copy()
# df["salary"] = df["salary"].astype(int)
# df_copy['salary'] = df_copy['salary'].apply(lambda x: x / 100000 )
# loc_salary = df_copy.groupby('location')['salary'].mean().sort_values(ascending=False)
# print(loc_salary.head(10))
# plt.figure()
# plt.bar(loc_salary.index, loc_salary.values, color='lightgreen')
# plt.title('Average Salary by Location')
# plt.xlabel('Location')
# plt.ylabel('Mean Salary')
# plt.show()


# Job Titles with Highest Salaries
# df_copy = df.copy()
# df["salary"] = df["salary"].astype(int)
# df_copy['salary'] = df_copy['salary'].apply(lambda x: x / 100000 )
# job_salary = df_copy.groupby('title')['salary'].mean().sort_values(ascending=False)
# plt.figure()
# plt.bar(job_salary.index, job_salary.values, color='lightgreen')
# plt.title('Average Salary by Job Title')
# plt.xlabel('Job Title')
# plt.xticks(rotation=35)
# plt.ylabel('Mean Salary')
# plt.show()


# TOp skills in demand
# skills_series = df["skills"].dropna().str.lower().str.split(", ")
# all_skills = sum(skills_series, [])
# skills_count = pd.Series(all_skills).value_counts().head(10)
# print(skills_count)
# plt.figure()
# skills_count.plot(kind="bar")
# plt.title("Top Skills in Demand")
# plt.xticks(rotation=45)
# plt.show()


# Top paying skills
# df_exploded = df.assign(skills=df['skills'].str.split(',')).explode('skills')
# df_exploded['skills'] = df_exploded['skills'].str.strip()
# df_exploded['salary'] = df_exploded['salary'].astype(int)
# df_exploded = df_exploded.groupby('skills')['salary'].mean().sort_values(ascending=False)
# plt.figure()
# df_exploded.plot(kind="bar")
# plt.title("Top Paying Skills")
# plt.show()


import csv
# import requests
from job.models import Job



# def scrape_jobs():
#     # resp = requests.get('https://jobicy.com/api/v2/remote-jobs')
#     resp = requests.get('https://remotive.com/api/remote-jobs')

#     if resp.status_code == 200:
#         data = resp.json()
#         for job in data['jobs']:
#             job = Job(
#                 title=job['title'],
#                 location=job['candidate_required_location'],
#                 company=job['company_name'],
#                 salary=job['salary'],
#                 description=job['description'],
#                 skills=','.join(job['tags'])
#             )
#             job.save()


def feed_jobs():
    with open('jobs_500.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'title':
                continue
            print(f"writing row {row[0]}")
            salary = None
            if len(row) > 3 and row[3]:
                try:
                    salary = int(row[3])
                except ValueError:
                    pass  # Salary remains None if conversion fails
            job = Job(
                title=row[0],
                company=row[1],
                location=row[2],
                salary=salary,
                description=row[4],
                skills=row[5]
            )
            job.save()

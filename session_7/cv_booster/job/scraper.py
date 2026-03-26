# import requests
from .models import Job
import csv


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
            if row[0] == "title":
                continue
            job = Job(
                title=row[0],
                company=row[1],
                location=row[2],
                salary=row[3],
                description=row[4],
                skills=row[5],
            )
            job.save()
            print(f"{job} saved to Database")
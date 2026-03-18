import requests
from .models import Job



def scrape_jobs():
    # resp = requests.get('https://jobicy.com/api/v2/remote-jobs')
    resp = requests.get('https://remotive.com/api/remote-jobs')

    if resp.status_code == 200:
        data = resp.json()
        for job in data['jobs']:
            job = Job(
                title=job['title'],
                location=job['candidate_required_location'],
                company=job['company_name'],
                salary=job['salary'],
                description=job['description'],
                skills=','.join(job['tags'])
            )
            job.save()

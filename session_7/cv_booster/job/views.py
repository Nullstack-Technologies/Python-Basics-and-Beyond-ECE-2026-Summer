from django.shortcuts import render
from django.http import HttpResponse

from .models import Job
import pandas as pd

def index(request):

    jobs = Job.objects.all()
    df = pd.DataFrame(jobs.values())

    total_jobs = int(df['title'].count())
    most_soughted_job = df['title'].value_counts()
    return render(
        request, 
        'index.html', 
        {'total_jobs': total_jobs, 'most_jobs': most_soughted_job}    
    )

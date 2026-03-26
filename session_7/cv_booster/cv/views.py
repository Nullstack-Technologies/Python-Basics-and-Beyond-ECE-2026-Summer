from django.shortcuts import render
from .forms import SalaryPredictionForm
from job.models import Job
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MultiLabelBinarizer

def index(request):
    predicted_salary = None
    form = SalaryPredictionForm(request.POST or None)
    error_message = None

    if request.method == 'POST' and form.is_valid():
        selected_skills = form.cleaned_data['skills']

        # 1. Prepare data for ML model
        jobs_with_data = Job.objects.exclude(salary__isnull=True).exclude(skills__in=['', None])
        
        job_data = [
            {
                'skills': [s.strip().lower() for s in job.skills.split(',') if s.strip()],
                'salary': job.salary
            }
            for job in jobs_with_data if job.skills
        ]

        if len(job_data) > 10: # Need a minimum amount of data to train
            df = pd.DataFrame(job_data)
            df = df[df['skills'].apply(len) > 0]

            # 2. Feature Engineering (One-Hot Encode skills)
            mlb = MultiLabelBinarizer()
            X = mlb.fit_transform(df['skills'])
            y = df['salary']

            # 3. Train Linear Regression Model
            model = LinearRegression()
            model.fit(X, y)

            # 4. Predict salary for selected skills
            input_vector = mlb.transform([selected_skills])
            predicted_salary = model.predict(input_vector)[0]
        else:
            error_message = "Not enough job data is available to make a salary prediction."

    context = {
        'form': form,
        'predicted_salary': predicted_salary / 100000, # convert to LPA
        'error_message': error_message,
    }
    return render(request, 'analyser.html', context)

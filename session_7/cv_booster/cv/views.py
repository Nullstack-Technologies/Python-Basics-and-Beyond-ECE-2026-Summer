from django.shortcuts import render
from job.models import Job
import pandas as pd
from cv.forms import SalaryPredictionForm
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MultiLabelBinarizer

def index(request):
    form = SalaryPredictionForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid():
        jobs = Job.objects.all()
        # selected skills
        selected_skills = form.cleaned_data['skills']
        
        job_data = [
            {
                'skills': [s.strip().lower() for s in job.skills.split(',')],
                'salary': job.salary
            }
            for job in jobs
        ]
        

        df = pd.DataFrame(job_data)
        
        # Preprocessing
        mlb = MultiLabelBinarizer()
        X = mlb.fit_transform(df['skills'])
        y = df['salary']

        # Linear Regression
        model = LinearRegression()
        model.fit(X,y)

        # Transform the input
        input_vector = mlb.transform([selected_skills])
        

        # Predict the value
        predicted_salary = model.predict(input_vector)
        predicted_salary = predicted_salary[0]

        context = {
            'form': form,
            'predicted_salary': round(predicted_salary / 100000, 2)    
        }

    return render(request, "analyser.html", context)
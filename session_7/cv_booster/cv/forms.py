from django import forms
from job.models import Job


class SalaryPredictionForm(forms.Form):
    skills = forms.MultipleChoiceField(
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        label="Select skills to predict salary",
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        skills_list = set()
        # This can be slow if there are many jobs.
        # A better approach for production would be a separate Skill model.
        jobs = Job.objects.exclude(skills__isnull=True).exclude(skills__exact='')
        for job in jobs:
            skills_list.update([s.strip().lower() for s in job.skills.split(',') if s.strip()])
        
        skill_choices = sorted([(skill, skill.capitalize()) for skill in skills_list])
        self.fields['skills'].choices = skill_choices
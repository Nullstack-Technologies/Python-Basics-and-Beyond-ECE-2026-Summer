from django import forms

from job.models import Job


class SalaryPredictionForm(forms.Form):
    skills = forms.MultipleChoiceField(
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        skills_list = set()
        jobs = Job.objects.all()
        for job in jobs:
            skills_list.update(
                [s.strip().lower() for s in job.skills.split(',')]
            )
        print(skills_list)
        skill_choices = sorted(
            [(skill, skill.capitalize()) for skill in skills_list]
        )
        self.fields['skills'].choices = skill_choices

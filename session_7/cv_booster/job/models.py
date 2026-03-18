from django.db import models


class Job(models.Model):

    title = models.CharField(max_length=300)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    salary = models.CharField(null=True, blank=True)
    description = models.TextField()
    skills = models.TextField()

    def __str__(self):
        return self.title

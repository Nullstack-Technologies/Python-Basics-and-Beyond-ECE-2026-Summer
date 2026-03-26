from django.urls import path, include

from .views import index

urlpatterns = [
    path('analyser/', index, name="cv-analyser")
]

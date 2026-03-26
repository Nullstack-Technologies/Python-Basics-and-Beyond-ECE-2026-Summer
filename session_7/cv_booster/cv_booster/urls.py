"""
URL configuration for cv_booster project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cv/', include('cv.urls')),
    path('', include('job.urls'))
]

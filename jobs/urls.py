# jobs/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('job-search/', views.job_search, name='job_search'),
    path('pricing/', views.pricing, name='pricing'),
    path('invite-friends/', views.invite_friends, name='invite_friends'),
]

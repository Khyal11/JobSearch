from django.contrib import admin
from django.urls import path, include
from jobs.views import index  # Import the index view function

urlpatterns = [
    path('', index, name='index'),  # Add this line for the root URL
    path('admin/', admin.site.urls),
    path('jobs/', include('jobs.urls')),
]

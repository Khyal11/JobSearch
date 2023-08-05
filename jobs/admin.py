from django.contrib import admin
from .models import Job  # Import the models you want to manage in the admin site

# Register your models with the admin site
admin.site.register(Job)

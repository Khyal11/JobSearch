# jobs/views.py

from django.shortcuts import render
from .models import Job
import logging



def index(request):
    return render(request, 'jobs\index.html')  # Assuming your index.html is in the templates folder


def job_search(request):
    if request.method == 'GET':
        keywords = request.GET.get('keywords', '')  # Provide an empty string as default
        location = request.GET.get('location', '')  # Provide an empty string as default

        # Filter jobs based on keywords and location
        job_results = Job.objects.filter(title__icontains=keywords, location__icontains=location)

        return render(request, 'jobs/job_search.html', {'job_results': job_results})

    return render(request, 'jobs/job_search.html')


def pricing(request):
    # Sample data for demonstration purposes
    pricing_data = [
        {
            'plan': 'Basic Plan',
            'price': '$9.99/month',
            'features': ['Feature 1', 'Feature 2', 'Feature 3'],
        },
        {
            'plan': 'Pro Plan',
            'price': '$19.99/month',
            'features': ['Feature A', 'Feature B', 'Feature C'],
        },
        # Add more plans and data as needed
    ]

    # Create a dictionary to store the context data
    context = {
        'pricing_data': pricing_data,
    }

    # Render the template with the context data
    return render(request, 'jobs/pricing.html', context)



def invite_friends(request):
    if request.method == 'POST':
        # Assuming you have a form with 'name' and 'email' fields
        name = request.POST.get('name')
        email = request.POST.get('email')

        # Send the invitation email
        logger = logging.getLogger('invite_friends')
        logger.info(f'Invitation sent to {name} at {email}')




        # Optionally, you can redirect to a "Thank You" page after sending the email
        return render(request, 'jobs/thank_you.html')

    return render(request, 'jobs/invite_friends.html')

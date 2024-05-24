# views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Email
from .email_utils import send_email

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        user = request.user  # Assuming user is authenticated
        content = request.POST.get('content')
        user_email = user.email

        # Email configuration
        sender_email = 'your_email@example.com'  # Your email address
        sender_password = 'your_password'  # Your email password
        subject = 'Welcome to our platform'  # Email subject

        try:
            # Send email
            send_email(sender_email, sender_password, user_email, subject, content)
        except RuntimeError as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

        # Save email to database
        email = Email(user=user, content=content)
        email.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


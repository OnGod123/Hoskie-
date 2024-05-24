# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        return HttpResponse('Invalid request method.')

def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        relationship_status = request.POST.get('relationship_status')
        sexual_orientation = request.POST.get('sexual_orientation')
        race = request.POST.get('race')
        phone_number = request.POST.get('phone_number')
        social_media_api = request.POST.get('social_media_api')
        birth_date = request.POST.get('birth_date')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Save the data to the database
        person = Person(
            name=name,
            relationship_status=relationship_status,
            sexual_orientation=sexual_orientation,
            race=race,
            phone_number=phone_number,
            social_media_api=social_media_api,
            birth_date=birth_date,
            email=email,
            password=password
        )
        person.save()

        try:
            # Send welcome email to the user
            send_welcome_email(name, email)
        except RuntimeError as e:
            return HttpResponse(str(e))

        return HttpResponse(f'Name: {name}, Email: {email}, Registration Successful. Check your email for a welcome message.')
    else:
        return HttpResponse('Invalid request method.')


        return HttpResponse(f'Name: {name}, Email: {email}')
    else:
        return HttpResponse('Invalid request method.')


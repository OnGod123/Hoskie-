# views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login
from .cache_auth import authenticate_user as cache_authenticate_user
from .models import User

def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        uuid = cache_authenticate_user(username_or_email, password)

        if uuid:
            # User authentication successful
            user = User.objects.get(uuid=uuid)
            login(request, user)  # Log the user in
            request.session['user_uuid'] = uuid
            request.session['username'] = user.username
            request.session['email'] = user.email
            return redirect('home')  # Redirect to the home page or user dashboard
        else:
            # Authentication failed
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def home_view(request):
    # Example view to show user details
    if request.user.is_authenticated:
        return render(request, 'home.html', {'user': request.user})
    else:
        return redirect('login')


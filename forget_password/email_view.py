from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import PasswordResetRequest
from django.contrib.auth.hashers import make_password

def update_password(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        token = request.GET.get('token')

        if not email or not token:
            return render(request, 'error.html', {'error': 'Invalid reset link'})

        # Check if the reset token is valid
        reset_request = PasswordResetRequest.objects.filter(user__email=email, token=token, is_active=True).first()
        if not reset_request:
            return render(request, 'error.html', {'error': 'Invalid reset link'})

        # Check if the reset link has expired
        if reset_request.created_at < timezone.now() - timezone.timedelta(hours=24):
            return render(request, 'error.html', {'error': 'Reset link has expired'})

        return render(request, 'update_password.html', {'email': email, 'token': token})

    elif request.method == 'POST':
        password = request.POST.get('password')

        # Validate the password
        if not password:
            return render(request, 'error.html', {'error': 'Password cannot be empty'})

        # Retrieve the user based on the email
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()

        # Update the user's password
        if user:
            user.password = make_password(password)
            user.save()

            # Authenticate the user with the new password
            user = authenticate(request, username=user.username, password=password)

            # If authentication succeeds, log in the user
            if user:
                signup(request, user)

                # Deactivate the password reset request
                token = request.POST.get('token')
                reset_request = PasswordResetRequest.objects.filter(user=user, token=token).first()
                if reset_request:
                    reset_request.is_active = False
                    reset_request.save()

                # Redirect the user to a success page or their profile page
                return redirect('profile')  # Redirect to the user's profile page

        # If authentication fails, or if the user does not exist, render an error page
        return render(request, 'error.html', {'error': 'Failed to update password'})


# views.py

from django.contrib.auth import authenticate, login
from django.core.cache import cache
from django.http import JsonResponse

def authenticate_user(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        user = authenticate(username=username_or_email, password=password)

        if user is not None:
            # User authentication successful
            uuid = str(user.uuid)

            # Store user data in session
            request.session['user_uuid'] = uuid
            request.session['username'] = user.username
            request.session['email'] = user.email

            login(request, user)  # Log the user in

            return JsonResponse({'uuid': uuid})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


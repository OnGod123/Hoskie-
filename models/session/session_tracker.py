# views.py

from django.contrib.sessions.models import Session
from django.http import JsonResponse

def track_user_activity(request):
    # Get session key
    session_key = request.session.session_key

    # Update session data
    request.session['last_activity'] = 'timestamp'

    return JsonResponse({'message': 'User activity tracked'})


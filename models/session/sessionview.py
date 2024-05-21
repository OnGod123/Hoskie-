# views.py

from django.contrib.sessions.models import Session
from django.http import JsonResponse

def track_user_activity(request):
    # Get session key
    session_key = request.session.session_key

    # Update session data
    request.session['last_activity'] = 'timestamp'

    return JsonResponse({'message': 'User activity tracked'})

def dashboard_view(request):
    session_key = request.session.session_key
    user_id = cache.get(f'session_{session_key}')
    
    if user_id:
        user = User.objects.get(id=user_id)
        context = {
            'user': user,
            'remaining_time': 21 * 24 * 60 * 60  # Assuming 3 weeks as the remaining time for simplicity
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('login')
def update_last_activity(request):
    if request.user.is_authenticated:
        session_key = request.session.session_key
        cache.set(f'session_{session_key}', request.user.id, timeout=60*60*24*21)  # Refresh cache for 3 weeks
    return JsonResponse({'status': 'ok'})

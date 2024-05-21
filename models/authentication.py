from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.cache import cache
from django.http import JsonResponse

def authenticate_user(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(username=username_or_email, password=password)

        if user is not None:
            # User authentication successful
            # Generate UUID and save it in session
            uuid = str(user.uuid)
            request.session['user_uuid'] = uuid

            return JsonResponse({'uuid': uuid})
        else:
            # User authentication failed
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def get_user_image_or_video(request):
    if request.method == 'GET':
        uuid = request.session.get('user_uuid')

        if uuid:
            # Fetch user based on UUID
            user = User.objects.filter(uuid=uuid).first()

            if user:
                # Logic to retrieve image or video from user instance
                image_url = user.image.url
                video_url = user.video.url

                return JsonResponse({'image_url': image_url, 'video_url': video_url})
            else:
                return JsonResponse({'error': 'User not found'}, status=404)
        else:
            return JsonResponse({'error': 'User not authenticated'}, status=401)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


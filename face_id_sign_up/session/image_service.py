# myapp/image_service.py

import os
from django.conf import settings
from asgiref.sync import sync_to_async
from .models import UserImage

class ImageService:
    @staticmethod
    def save_image_to_media(user, image_data):
        # Generate file path
        file_path = os.path.join(settings.MEDIA_ROOT, 'images', f'{user.username}_image.jpg')
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Write image data to file
        with open(file_path, 'wb') as f:
            f.write(image_data)
        
        return file_path

    @staticmethod
    async def create_user_image_instance(user, file_path):
        # Create UserImage instance and save it
        user_image = UserImage(user=user, image=file_path)
        await sync_to_async(user_image.save)()


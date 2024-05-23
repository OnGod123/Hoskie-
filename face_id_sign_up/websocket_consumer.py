# myapp/consumers.py

import base64
import os
import redis
from django.conf import settings
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import CustomUser, UserImage

class ImageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            # Save image to Redis temporarily
            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
            redis_client.set('image_data', bytes_data)

            # Save image to media directory and create a UserImage instance
            user = await sync_to_async(CustomUser.objects.get)(username=self.scope["user"].username)
            file_path = os.path.join(settings.MEDIA_ROOT, 'images', f'{user.username}_image.jpg')
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'wb') as f:
                f.write(bytes_data)

            # Create UserImage instance
            user_image = UserImage(user=user, image=file_path)
            await sync_to_async(user_image.save)()

            # Optionally send a confirmation message back to the client
            await self.send(text_data='Image received and saved successfully.')


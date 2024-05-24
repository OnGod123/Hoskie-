# myapp/consumers.py

from channels.generic.websocket import AsyncWebsocketConsumer
from .session_manager import SessionManager
from .image_service import ImageService

class ImageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        if self.user.is_authenticated:
            self.session_manager = SessionManager()
            self.image_service = ImageService()
            self.session_uuid = self.session_manager.create_session(self.user.id)
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        self.session_manager.delete_session(self.session_uuid)

    async def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            await self.handle_image_upload(bytes_data)

    async def handle_image_upload(self, bytes_data):
        # Register the event
        self.session_manager.register_event(self.session_uuid, 'image_upload')

        # Save image data to Redis
        self.session_manager.save_image_data(self.session_uuid, bytes_data)

        # Save image to media directory
        file_path = self.image_service.save_image_to_media(self.user, bytes_data)

        # Create UserImage instance
        await self.image_service.create_user_image_instance(self.user, file_path)

        # Optionally send a confirmation message back to the client
        await self.send(text_data='Image received and saved successfully.')


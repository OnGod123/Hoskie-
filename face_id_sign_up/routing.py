# myapp/routing.py

from django.urls import re_path
from .consumers import ImageConsumer

websocket_urlpatterns = [
    re_path(r'ws/image/$', ImageConsumer.as_asgi()),
]


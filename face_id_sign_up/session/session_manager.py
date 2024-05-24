# myapp/session_manager.py

import uuid
import redis
from django.conf import settings

class SessionManager:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)
        self.sessions = {}

    def create_session(self, user_uuid):
        session_uuid = str(uuid.uuid4())
        self.sessions[session_uuid] = {
            'user_uuid': user_uuid,
            'state': {},
            'events': []
        }
        return session_uuid

    def get_session(self, session_uuid):
        return self.sessions.get(session_uuid)

    def register_event(self, session_uuid, event):
        if session_uuid in self.sessions:
            self.sessions[session_uuid]['events'].append(event)

    def set_user_state(self, session_uuid, state):
        if session_uuid in self.sessions:
            self.sessions[session_uuid]['state'] = state

    def get_user_state(self, session_uuid):
        if session_uuid in self.sessions:
            return self.sessions[session_uuid].get('state')

    def save_image_data(self, session_uuid, image_data):
        if session_uuid in self.sessions:
            key = f'{session_uuid}_image_data'
            self.redis_client.set(key, image_data)

    def get_image_data(self, session_uuid):
        key = f'{session_uuid}_image_data'
        return self.redis_client.get(key)

    def delete_session(self, session_uuid):
        if session_uuid in self.sessions:
            key = f'{session_uuid}_image_data'
            self.redis_client.delete(key)
            del self.sessions[session_uuid]


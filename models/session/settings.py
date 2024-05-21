# settings.py

# Configure session middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Other middleware classes...
]

# Configure session engine
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # Example: Use cache backend
SESSION_CACHE_ALIAS = 'default'  # Use default cache backend


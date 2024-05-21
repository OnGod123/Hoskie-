from django.core.cache import cache

def authenticate_user(username_or_email, password):
    # Check number of sign-in attempts
    sign_in_attempts = cache.get('sign_in_attempts', 0)

    if sign_in_attempts <= 1:
        # Attempt authentication via database
        from . import db_auth  # Importing database authentication logic
        uuid = db_auth.authenticate_user(username_or_email, password)

        if uuid:
            # User authentication successful
            # Save UUID in cache
            cache_key = f'user_credentials_{username_or_email}_{password}'
            cache.set(cache_key, uuid, timeout=None)

            # Increment sign-in attempts counter
            cache.set('sign_in_attempts', sign_in_attempts + 1)

            return uuid
    else:
        # Exceeded maximum sign-in attempts, switch to cache authentication
        cache_key = f'user_credentials_{username_or_email}_{password}'
        cached_uuid = cache.get(cache_key)

        if cached_uuid:
            # User authentication successful
            return cached_uuid

    # Authentication failed
    return None


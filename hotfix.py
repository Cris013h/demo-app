def validate_token(token):
    # FIX: added expiry check
    if token.is_expired():
        raise Exception("Token expired")
    return True

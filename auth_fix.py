def login(user, password):
    # FIX: token now expires after 24 hours
    token = generate_token(user, expires_in=86400)
    return token
  

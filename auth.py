def login(user, password):
    # BUG: token never expires
    token = generate_token(user)
    return token

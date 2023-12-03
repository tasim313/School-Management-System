import hashlib

def custom_hashing_logic(password):
    
    if password is None:
        return None

    password_bytes = password.encode('utf-8')

    hashed_password = hashlib.sha256(password_bytes).hexdigest()

    return hashed_password
import bcrypt

# Hash Password

def hash_password(password):

    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

# Verify Password

def verify_password(password, hashed):

    return bcrypt.checkpw(
        password.encode(),
        hashed
    )
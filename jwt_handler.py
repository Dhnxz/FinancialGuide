import jwt
import datetime

SECRET_KEY = "finance_secret"

def create_token(username):

    payload = {

        "username": username,

        "exp":
        datetime.datetime.utcnow()
        + datetime.timedelta(hours=2)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )

    return token
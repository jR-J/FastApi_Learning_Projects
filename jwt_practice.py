import jwt
from datetime import datetime, timedelta, timezone

#server config
SECRET_KEY = "helpdesk"
ALGORITHM ="HS256"

#create jwt login token
def create_login_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)) -> str:

    #copy of data to not mess up original data
    to_encode = data.copy()

    #expiration time
    expire = datetime.now(timezone.utc)+expires_delta
    to_encode.update({"exp":expire})

    #encode and sign the token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

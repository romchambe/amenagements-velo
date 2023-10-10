from datetime import datetime, timedelta
import os
import jwt


jwt_secret = os.getenv("JWT_SECRET_KEY")


class WithToken:
    request_token: str


def encode_jwt(payload: dict[str, str]) -> str:
    return jwt.encode(payload, jwt_secret)


def decode_token(token) -> str:
    token_data = jwt.get_unverified_header(token)

    payload = jwt.decode(
        token,
        key=jwt_secret,
        algorithms=[token_data['alg'], ],
        options={"require": ["exp", "sub"]}
    )

    return payload['sub']


def create_token() -> tuple[str, str]:
    # Create cache key with expiration
    id = 'test'

    return id, encode_jwt({
        'sub': id,
        'exp': datetime.now() + timedelta(hours=1)
    })

import hashlib
import json


def sign_message(message: dict, secret: str):
    payload = json.dumps(message, sort_keys=True).encode()
    return hashlib.sha256(payload + secret.encode()).hexdigest()


def verify_signature(message: dict, secret: str):
    if "signature" not in message:
        return False
    clean = {k: v for k, v in message.items() if k != "signature"}
    return sign_message(clean, secret) == message["signature"]

import hashlib
import json
from datetime import datetime


def sign_payload(payload: dict, secret: str):
    raw = json.dumps(payload, sort_keys=True).encode()
    return hashlib.sha256(raw + secret.encode()).hexdigest()


def verify_payload(payload: dict, secret: str):
    if "signature" not in payload:
        return False
    clean = {k: v for k, v in payload.items() if k != "signature"}
    return sign_payload(clean, secret) == payload["signature"]

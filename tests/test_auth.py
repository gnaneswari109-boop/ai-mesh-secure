import pytest
from app.services.auth import sign_message, verify_signature


def test_sign_message():
    message = {"sender": "agent-1", "content": "hello"}
    secret = "secret-key"
    signature = sign_message(message, secret)
    assert isinstance(signature, str)
    assert len(signature) == 64  # SHA256 hex


def test_verify_signature():
    message = {"sender": "agent-1", "content": "hello"}
    secret = "secret-key"
    signature = sign_message(message, secret)
    message["signature"] = signature
    assert verify_signature(message, secret) is True


def test_verify_signature_invalid():
    message = {"sender": "agent-1", "content": "hello", "signature": "invalid"}
    secret = "secret-key"
    assert verify_signature(message, secret) is False

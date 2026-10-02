import json
import redis

from app.config import get_settings

settings = get_settings()

try:
    redis_client = redis.Redis.from_url(settings.redis_url, decode_responses=True)
    redis_client.ping()
except Exception:
    redis_client = None


def emit(topic: str, payload: dict):
    if redis_client is None:
        return
    redis_client.publish(topic, json.dumps(payload))

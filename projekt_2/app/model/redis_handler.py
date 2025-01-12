import json

import redis

r = redis.Redis(host='localhost', port=6379, db=0)

class RedisHandler:

    def __init__(self, redis_instance):
        self.redis = redis_instance

    def get_data(self, key):
        data = self.redis.get(key)
        if data:
            return json.loads(data.decode('utf-8'))
        return []

    def set_data(self, key, value):
        encoded_value = json.dumps(value)
        self.redis.set(key, encoded_value)

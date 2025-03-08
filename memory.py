import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def set_memory(key, value):
    r.set(key, value)

def get_memory(key):
    return r.get(key)
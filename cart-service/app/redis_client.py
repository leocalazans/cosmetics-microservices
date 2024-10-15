import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def add_item_to_cart(user_id, item):
    cart_key = f"cart:{user_id}"
    redis_client.hincrby(cart_key, item.product_id, item.quantity)

def get_cart(user_id):
    cart_key = f"cart:{user_id}"
    return redis_client.hgetall(cart_key)

def clear_cart(user_id):
    cart_key = f"cart:{user_id}"
    redis_client.delete(cart_key)

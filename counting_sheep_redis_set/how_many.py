from redis import Redis

redis_conn = Redis()

SHEEP_SET_KEY = "sheep_seen"

redis_conn.delete(SHEEP_SET_KEY)

redis_conn.sadd(SHEEP_SET_KEY, "1934")
redis_conn.sadd(SHEEP_SET_KEY, "1201")
redis_conn.sadd(SHEEP_SET_KEY, "1199")
redis_conn.sadd(SHEEP_SET_KEY, "0007")
redis_conn.sadd(SHEEP_SET_KEY, "3409")
redis_conn.sadd(SHEEP_SET_KEY, "1934")
redis_conn.sadd(SHEEP_SET_KEY, "1015")

print(f"There are {redis_conn.scard(SHEEP_SET_KEY)} sheep.")
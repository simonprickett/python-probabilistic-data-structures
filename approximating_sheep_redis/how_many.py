from redis import Redis

redis_conn = Redis()

SHEEP_SET_KEY = "sheep_seen"
SHEEP_HLL_KEY = "sheep_seen_hll"

redis_conn.delete(SHEEP_SET_KEY)
redis_conn.delete(SHEEP_HLL_KEY)

for m in range(0, 100000):
    sheep_id = str(m)
    pipeline = redis_conn.pipeline(transaction=False)
    pipeline.sadd(SHEEP_SET_KEY, sheep_id)
    pipeline.pfadd(SHEEP_HLL_KEY, sheep_id)
    pipeline.execute()

print(f"There are {redis_conn.scard(SHEEP_SET_KEY)} sheep (set: {redis_conn.memory_usage(SHEEP_SET_KEY)}).")
print(f"There are {redis_conn.pfcount(SHEEP_HLL_KEY)} sheep (hyperloglog: {redis_conn.memory_usage(SHEEP_HLL_KEY)}).")
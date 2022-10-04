from redis import Redis

redis_conn = Redis()

SHEEP_BLOOM_KEY = "sheep_seen_bloom"

redis_conn.delete(SHEEP_BLOOM_KEY)
redis_conn.bf().create(SHEEP_BLOOM_KEY, 0.001, 200000, noScale = True)

for m in range(0, 100000):
    sheep_id = str(m)
    redis_conn.bf().add(SHEEP_BLOOM_KEY, sheep_id)

def have_i_seen(sheep_id):
    if redis_conn.bf().exists(SHEEP_BLOOM_KEY, sheep_id):
        print(f"I might have seen sheep {sheep_id}.")
    else:
        print(f"I have not seen sheep {sheep_id}.")

have_i_seen("9018")
have_i_seen("454991")
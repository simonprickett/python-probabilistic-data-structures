from redis import Redis

redis_conn = Redis()

SHEEP_SET_KEY = "sheep_seen"

redis_conn.delete(SHEEP_SET_KEY)
redis_conn.sadd(SHEEP_SET_KEY, "1934", "1201", "1199", "0007", "3409", "1015")

def have_i_seen(sheep_id):
    if redis_conn.sismember(SHEEP_SET_KEY, sheep_id):
        print(f"I have seen sheep {sheep_id}.")
    else:
        print(f"I have not seen sheep {sheep_id}.")

have_i_seen("1934")
have_i_seen("1283")
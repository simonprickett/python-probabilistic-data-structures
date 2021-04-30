from hyperloglog import HyperLogLog
from sys import getsizeof

sheep_seen = set()
sheep_seen_hll = HyperLogLog(0.01)

for m in range(0, 2000000):
    sheep_id = str(m)
    sheep_seen.add(sheep_id)
    sheep_seen_hll.add(sheep_id)

print(f"There are {len(sheep_seen)} sheep (set: {getsizeof(sheep_seen)}).")
print(f"There are {len(sheep_seen_hll)} sheep (hyperloglog: {getsizeof(sheep_seen_hll)}).")
from hyperloglog import HyperLogLog

sheep_seen = set()
sheep_seen_hll = HyperLogLog(0.01)

for m in range(0, 100000):
    sheep_id = str(m)
    sheep_seen.add(sheep_id)
    sheep_seen_hll.add(sheep_id)

print(f"There are {len(sheep_seen)} sheep (set).")
print(f"There are {len(sheep_seen_hll)} sheep (hyperloglog).")
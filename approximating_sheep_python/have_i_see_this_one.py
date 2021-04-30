from probables import BloomFilter

sheep_seen_bloom = BloomFilter(
    est_elements=200000, false_positive_rate=0.01
)

for m in range(0, 100000):
    sheep_id = str(m)
    sheep_seen_bloom.add(sheep_id)

def have_i_seen(sheep_id):
    if sheep_seen_bloom.check(sheep_id):
        print(f"I might have seen sheep {sheep_id}.")
    else:
        print(f"I have not seen sheep {sheep_id}.")

have_i_seen("9018")
have_i_seen("454991")



# No, Maybe and Close Enough!

Exploring Probabilistic Data Structures in Python - my 2021 Pycon USA and Australia talk.  I've updated the code slightly for Pycon MEA Dubai 2022 - it now uses the latest redis-py Redis client.

If you'd like to see the slides for the 2021 version of this talk, they're [here](https://simonprickett.dev/no_maybe_and_close_enough_slides.pdf) (PDF).  Watch the 2021 video [here](https://www.youtube.com/watch?v=hM1JPkEUtks) or [read the transcript on my website](https://simonprickett.dev/no-maybe-and-good-enough-probabilistic-data-structures-in-python/).  I gave a shorter version of this talk in person for Pycon MEA Dubai 2022 - [watch that here](https://www.youtube.com/watch?v=tqy8WtjBe1Q).

This repository contains supporting code to run the examples from my talk.  The example code uses in memory probabilistic data structures with the [hyperloglog](https://pypi.org/project/hyperloglog/) and [pyprobables](https://pypi.org/project/pyprobables/) libraries.  It also uses [Redis](https://redis.io) with the [RedisBloom](https://redisbloom.io) module: this is provided for you as part of [Redis Stack](https://redis.io/docs/stack/get-started/) in a Docker container.

The two probabilistic data structures examined in this code base are:

* [HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog) - an algorithm for estimating the cardinality of a set (the count distinct problem)
* [Bloom Filter](https://en.wikipedia.org/wiki/Bloom_filter) - a data structure used to determine whether an element may be a member of a set

## Setup

To run the example code and Redis server, you will need both Python 3 (I've tested this with 3.8.6) and [Docker](https://www.docker.com/).  Once you have these, clone the repo, create a virtual environment, and start the Docker container in the background:

```bash
$ git clone https://github.com/simonprickett/python-probabilistic-data-structures.git
$ cd python-probabilistic-data-structures
$ python3 -m venv venv
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ docker compose up -d
```

The Docker container uses port 6379. If you have another process (example: an existing Redis server instance) listening on that port, stop that process before starting the container.

## Running the Examples

### Counting Sheep

These examples use a Python set, then a Redis set to count sheep.  They give an accurate count, but at the cost of memory usage.  Moving the count to a Redis set offloads the memory usage problem to Redis, and solves the problem of allowing multiple instances of the Python code to work together to count sheep.

Counting sheep in memory with a Python set:

```bash
(venv) $ cd counting_sheep_python
(venv) $ python how_many.py
There are 6 sheep.
```

Have I seen this sheep in memory with a Python set:

```bash
(venv) $ python have_i_seen_this_one.py
I have seen sheep 1934.
I have not seen sheep 1283.
```

Counting sheep with a Redis set:

```bash
(venv) $ cd ../counting_sheep_redis
(venv) $ python how_many.py
There are 6 sheep
```

Have I seen this sheep with a Redis set:

```bash
(venv) $ python have_i_seen_this_one.py
I have seen sheep 1934.
I have not seen sheep 1283.
```

## Approximating Sheep

These examples use the HyperLogLog to approximate a count of sheep seen, and the Bloom Filter to determine whether or not a particular sheep has been seen. They use both in memory Python implementations of the probabilistic data structures, and the Redis equivalents.

Approximate count with Python in memory HyperLogLog, compares count with an in memory set:

```bash
(venv) $ cd ../approximating_sheep_python
(venv) $ python how_many.py
There are 100000 sheep (set).
There are 100075 sheep (hyperloglog).
```
Have I (maybe) seen this sheep with Python in memory Bloom Filter:

```bash
(venv) $ python have_i_see_this_one.py
I might have seen sheep 9018.
I have not seen sheep 454991.
```

Approximate count with Redis HyperLogLog:

```bash
(venv) $ cd ../approximating_sheep_redis
(venv) $ python how_many.py
There are 100000 sheep (set: 4673012).
There are 99565 sheep (hyperloglog: 12366).
```

Have I (maybe) seen this sheep with Redis Bloom Filter:

```bash
(venv) $ python have_i_seen_this_one.py
I might have seen sheep 9018.
I have not seen sheep 454991.
```


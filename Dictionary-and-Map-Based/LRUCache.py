# Implement a Basic Cache Using Python's Dictionary (LRU Cache)
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)  # Move accessed item to the end to mark it as recently used
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)  # Move existing item to the end
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove the least recently used item


# Uses OrderedDict to maintain order and evict least recently used items when the capacity is exceeded.

cache = LRUCache(2)  # Cache capacity of 2
cache.put(1, 1)      # Cache is {1=1}
cache.put(2, 2)      # Cache is {1=1, 2=2}
print(cache.get(1))  # Output: 1 (Cache is {2=2, 1=1})
cache.put(3, 3)      # LRU key 2 is removed, Cache is {1=1, 3=3}
print(cache.get(2))  # Output: -1 (2 was evicted)
cache.put(4, 4)      # LRU key 1 is removed, Cache is {3=3, 4=4}
print(cache.get(1))  # Output: -1 (1 was evicted)
print(cache.get(3))  # Output: 3 (Cache is {4=4, 3=3})
print(cache.get(4))  # Output: 4 (Cache is {3=3, 4=4})

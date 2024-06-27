class MyHashSet:

    def __init__(self):
        self.capacity = 1000  # Choose a reasonable initial capacity
        self.buckets = [None] * self.capacity

    def _hash(self, key):
        return key % self.capacity

    def add(self, key):
        hash_key = self._hash(key)
        if not self.buckets[hash_key]:
            self.buckets[hash_key] = [key]
        else:
            if key not in self.buckets[hash_key]:
                self.buckets[hash_key].append(key)

    def remove(self, key):
        hash_key = self._hash(key)
        if self.buckets[hash_key]:
            if key in self.buckets[hash_key]:
                self.buckets[hash_key].remove(key)

    def contains(self, key):
        hash_key = self._hash(key)
        return self.buckets[hash_key] and key in self.buckets[hash_key]


# class MyHashSet:

#     def hash_function(self, key):
#         key = key%1000000
#         return key
        
#     def __init__(self):
#         self.bucket = {}

#     def add(self, key: int) -> None:
#         hash_val = self.hash_function(key)
#         if hash_val in self.bucket:
#             if key not in self.bucket[hash_val]:
#                 self.bucket[hash_val].append(key)
#         else:
#             self.bucket[hash_val] = [key]

#     def remove(self, key: int) -> None:
#         hash_val = self.hash_function(key)
#         if hash_val in self.bucket:
#             if key in self.bucket[hash_val]:
#                 self.bucket[hash_val].remove(key)

#     def contains(self, key: int) -> bool:
#         hash_val = self.hash_function(key)
#         if hash_val in self.bucket:
#             for val in self.bucket[hash_val]:
#                 if key == val:
#                     return True
#         return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
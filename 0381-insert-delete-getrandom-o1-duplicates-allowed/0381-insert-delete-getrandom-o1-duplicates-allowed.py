from collections import defaultdict
from random import choice

class RandomizedCollection:
    # https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/editorial/
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.hm = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.hm[val].add(len(self.values))
        self.values.append(val)
        return len(self.hm[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.hm[val]: return False
        remove, last = self.hm[val].pop(), self.values[-1]
        self.values[remove] = last
        self.hm[last].add(remove)
        self.hm[last].discard(len(self.values) - 1)

        self.values.pop()
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.values)



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
from sortedcontainers import SortedSet
class NumberContainers:
    # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2349.Design%20a%20Number%20Container%20System
    def __init__(self):
        self.numbers = defaultdict(int)
        self.idx_hm = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        if index in self.numbers:
            self.idx_hm[self.numbers[index]].remove(index)
        self.numbers[index] = number
        self.idx_hm[number].add(index)        

    def find(self, number: int) -> int:
        if len(self.idx_hm[number]) > 0:
            return self.idx_hm[number][0]       
        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
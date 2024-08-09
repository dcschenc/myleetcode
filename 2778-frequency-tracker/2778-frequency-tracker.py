class FrequencyTracker:

    def __init__(self):
        self.cnt = {}        
        self.frequencies = defaultdict(int)

    def add(self, number: int) -> None:        
        if number in self.cnt:
            self.frequencies[self.cnt[number]] -= 1
            self.cnt[number] += 1
            self.frequencies[self.cnt[number]] += 1
        else:
            self.cnt[number] = 1
            self.frequencies[self.cnt[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.cnt:
            self.frequencies[self.cnt[number]] -= 1
            self.cnt[number] -= 1
            if self.cnt[number] == 0:
                del self.cnt[number]
            else:
                self.frequencies[self.cnt[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequencies[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
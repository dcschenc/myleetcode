class TwoSum:
    def __init__(self):
        self.data = []
        self.is_sorted = False        

    def add(self, number: int) -> None:
        self.data.append(number)
        self.is_sorted = False

    def find(self, value: int) -> bool:
        if self.is_sorted is False:
            self.data.sort()
            self.is_sorted = True
            
        l, r = 0, len(self.data) - 1
        while l < r:
            cur = self.data[l] + self.data[r]
            if cur < value:
                l += 1
            elif cur > value:
                r -= 1
            else:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
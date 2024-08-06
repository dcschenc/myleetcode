class DataStream:
    # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2526.Find%20Consecutive%20Integers%20from%20a%20Data%20Stream
    
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.cnt = 0        

    def consec(self, num: int) -> bool:
        if num != self.value:
            self.cnt = 0
        else:
            self.cnt += 1
            if self.cnt >= self.k:
                return True
        return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        cur = 0
        for n in nums:
            cur += n
            self.prefix.append(cur)
        
        
    def sumRange(self, left: int, right: int) -> int:
        r = self.prefix[right] 
        l = self.prefix[left - 1] if left > 0 else 0
        return r - l

    # def __init__(self, nums: List[int]):
    #     self.nums = nums
    #     self.sum = [0]
    #     for i in range(len(nums)):
    #         # if i == 0:
    #         #     self.sum[i] = nums[i]
    #         # else:
    #         self.sum.append(self.sum[i] + nums[i])
        

    # def sumRange(self, left: int, right: int) -> int:
    #     # return sum(self.nums[left:right+1])
    #     # return self.sum[right] - self.sum[left] + self.sum[left]
    #     return self.sum[right+1] - self.sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
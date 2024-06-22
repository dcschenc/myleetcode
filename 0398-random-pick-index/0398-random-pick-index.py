class Solution:

    def __init__(self, nums: List[int]):
        self.hm = defaultdict(list)
        for i, num in enumerate(nums):
            self.hm[num].append(i)
        

    def pick(self, target: int) -> int:
        choices = self.hm[target]
        return random.choice(choices)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                cnt += 1
        if cnt % 2 == 0:
            return 1
        return -1
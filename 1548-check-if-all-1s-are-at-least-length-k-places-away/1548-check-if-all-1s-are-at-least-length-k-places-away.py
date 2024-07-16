class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        left = -1
        for i, c in enumerate(nums):
            if c == 1:
                if left != -1 and i - left - 1 < k:
                    return False
                left = i
        return True
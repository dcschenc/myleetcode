class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = 0
        for left in range(len(nums)):
            if left > right:
                return False
            # if nums[i] > 0:
            right = max(right, left + nums[left])
                # if curr + nums[i] > right:
                    # right = curr
        return True
            
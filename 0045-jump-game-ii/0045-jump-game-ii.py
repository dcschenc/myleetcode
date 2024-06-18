class Solution:
    def jump(self, nums: List[int]) -> int:
        right = nums[0]
        cur, steps = 0, 0

        for i in range(len(nums)):
            if cur < i:
                steps += 1
                cur = right
            right = max(right, i + nums[i])       
            # if i + nums[i] > right:
                # right = i + nums[i]
        return steps
                
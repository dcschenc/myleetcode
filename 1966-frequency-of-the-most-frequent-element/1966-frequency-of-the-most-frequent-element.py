class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1838.Frequency%20of%20the%20Most%20Frequent%20Element
        nums.sort()
        left = ans = total = 0

        for right in range(len(nums)):
            target = nums[right]
            total += target
            
            while (right - left + 1) * target - total > k:
                total -= nums[left]
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans        
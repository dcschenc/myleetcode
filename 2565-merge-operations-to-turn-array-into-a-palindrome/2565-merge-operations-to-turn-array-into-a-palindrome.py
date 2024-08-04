class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2422.Merge%20Operations%20to%20Turn%20Array%20Into%20a%20Palindrome
        i, j = 0, len(nums) - 1
        cnt = 0
        while i < j:
            if nums[i] == nums[j]:
                i += 1
                j -= 1
            elif nums[i] < nums[j]:
                i += 1
                nums[i] += nums[i - 1]
                cnt += 1
            else:
                j -= 1
                nums[j] += nums[j + 1]
                cnt += 1
        return cnt
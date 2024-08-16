class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3000-3099/3034.Number%20of%20Subarrays%20That%20Match%20a%20Pattern%20I
        n, m = len(nums), len(pattern)
        ans = 0
        for i in range(n - m):
            j = i + 1
            for k in range(m):
                if pattern[k] == 1:
                    if nums[j] <= nums[j-1]:
                        break
                elif pattern[k] == 0:
                    if nums[j] != nums[j-1]:
                        break
                else:
                    if nums[j] >= nums[j-1]:
                        break
                j += 1
            if j - i - 1 == m:
                ans += 1
        return ans
            
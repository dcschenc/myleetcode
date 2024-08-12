class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2831.Find%20the%20Longest%20Equal%20Subarray
        cnt = Counter()
        left = 0
        mx = 0
        for right, x in enumerate(nums):
            cnt[x] += 1
            mx = max(mx, cnt[x])
            if right - left + 1 - mx > k:
                cnt[nums[left]] -= 1
                left += 1
        return mx
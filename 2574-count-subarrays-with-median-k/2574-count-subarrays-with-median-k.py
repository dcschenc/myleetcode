class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2488.Count%20Subarrays%20With%20Median%20K
        i = nums.index(k)
        cnt = Counter()
        ans = 1
        x = 0
        for v in nums[i + 1 :]:
            x += 1 if v > k else -1
            ans += 0 <= x <= 1
            cnt[x] += 1
        x = 0
        for j in range(i - 1, -1, -1):
            x += 1 if nums[j] > k else -1
            ans += 0 <= x <= 1
            ans += cnt[-x] + cnt[-x + 1]
        return ans
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2841.Maximum%20Sum%20of%20Almost%20Unique%20Subarray
        cnt = Counter(nums[:k])
        s = sum(nums[:k])
        ans = s if len(cnt) >= m else 0
        for i in range(k, len(nums)):
            cnt[nums[i]] += 1
            cnt[nums[i - k]] -= 1
            s += nums[i] - nums[i - k]
            if cnt[nums[i - k]] == 0:
                cnt.pop(nums[i - k])
            if len(cnt) >= m:
                ans = max(ans, s)
        return ans
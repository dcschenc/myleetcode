class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cnt = Counter({0: 1})
        ans = cur = 0
        for num in nums:
            if num == 1:
                cur += 1
            ans += cnt[cur - goal]
            cnt[cur] += 1
        return ans

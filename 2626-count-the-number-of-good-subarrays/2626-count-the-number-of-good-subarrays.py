class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2537.Count%20the%20Number%20of%20Good%20Subarrays
        cnt = Counter()
        ans = cur = 0
        i = 0
        for x in nums:
            cur += cnt[x]
            cnt[x] += 1
            while cur - cnt[nums[i]] + 1 >= k:
                cnt[nums[i]] -= 1
                cur -= cnt[nums[i]]
                i += 1
            if cur >= k:
                ans += i + 1
        return ans

        # n = len(nums)
        # prepairs = [0] * n
        # hm = defaultdict(int)
        # hm[nums[0]] = 1
        # for i in range(1, n):
        #     if nums[i] in s:
        #         prepairs[i] = prepairs[i-1] + hm[nums[i]]
        #     hm[nums[i]] += 1
        # ans = 0
        # for i in range(1, n):
        #     if prepairs[]
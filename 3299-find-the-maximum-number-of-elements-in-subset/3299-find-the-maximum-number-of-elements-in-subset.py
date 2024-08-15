class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3000-3099/3020.Find%20the%20Maximum%20Number%20of%20Elements%20in%20Subset
        cnt = Counter(nums)
        ans = cnt[1] - (cnt[1] % 2 ^ 1)
        del cnt[1]
        for x in cnt:
            t = 0
            while cnt[x] > 1:
                x = x * x
                t += 2
            t += 1 if cnt[x] else -1
            ans = max(ans, t)
        return ans

        # cnt = Counter(nums)
        # ans = 1
        # for num in cnt.keys():
        #     if cnt[num] < 2:
        #         continue
        #     if num == 1:
        #         if cnt[num] % 2 == 0:
        #             ans = max(ans, cnt[num] - 1)
        #         else:
        #             ans = max(ans, cnt[num])
        #         continue
        #     k = 2
        #     while num ** k in cnt and cnt[num ** k] >= 2:
        #         k *= 2
        #     if num ** k in cnt and cnt[num ** k] == 1:
        #         ans = max(ans, k + 1 if (k + 1) % 2 == 1 else k )
        #     else:
        #         ans = max(ans, (int(log(k, 2)) - 1) * 2 + 1)
        # return ans
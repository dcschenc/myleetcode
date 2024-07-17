class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1498.Number%20of%20Subsequences%20That%20Satisfy%20the%20Given%20Sum%20Condition
        mod = 10 ** 9 + 7
        nums.sort()
        ans = 0
        for i, num in enumerate(nums):
            if num * 2 > target:
                break
            j = bisect_right(a = nums, x = target - num, lo = i  + 1) - 1
            ans = (ans + 2 ** (j - i)) % mod
        return ans

        # hm = defaultdict(int)
        # ans = 0
        # for i, num in enumerate(nums):
        #     if 2 * num <= target:
        #         hm[(num, num)] += 1
        #         ans += 1
        #     keys = list(hm.keys())
        #     for mi, mx in keys:
        #         if mx == num:
        #             hm[(mi, mx)] += 1
        #             ans += hm[(mi, mx)]
        #         elif mi + num <= target:                    
        #             hm[(mi, num)] = hm[(mi, mx)]
        #             ans += hm[(mi, num)] 
        # return ans % mod


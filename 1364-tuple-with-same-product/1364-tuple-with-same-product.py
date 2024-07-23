class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1726.Tuple%20with%20Same%20Product
        # cnt = defaultdict(int)
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         x = nums[i] * nums[j]
        #         cnt[x] += 1
        # return sum(v * (v - 1) // 2 for v in cnt.values()) << 3

        n = len(nums)
        ans = 0
        # nums.sort()
        hm = defaultdict(int)
        for a in range(n):
            for b in range(a + 1, n):
                ab = nums[a] * nums[b]
                hm[ab] += 1
        return sum(v * (v - 1) // 2 for v in hm.values()) * 8
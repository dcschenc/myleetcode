class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2811.Check%20if%20it%20is%20Possible%20to%20Split%20Array
        @cache
        def backtrack(i, j):
            if i + 1 == j:
                return True
            for k in range(i + 1, j):
                if k - i > 1 and presum[k] - presum[i] < m or j - k > 1 and presum[j] - presum[k] < m:
                    continue
                if backtrack(i, k) and backtrack(k, j):
                    return True
            return False
        
        presum, n, cur = [0], len(nums), 0
        for i in range(n):
            cur += nums[i]
            presum.append(cur)

        res = backtrack(0, n)
        return res
        
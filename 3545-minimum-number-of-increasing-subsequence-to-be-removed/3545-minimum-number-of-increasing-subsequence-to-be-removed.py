class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3200-3299/3231.Minimum%20Number%20of%20Increasing%20Subsequence%20to%20Be%20Removed
        g = []
        for x in nums:
            l, r = 0, len(g)
            while l < r:
                mid = (l + r) >> 1
                if g[mid] < x:
                    r = mid
                else:
                    l = mid + 1
            if l == len(g):
                g.append(x)
            else:
                g[l] = x
        return len(g)
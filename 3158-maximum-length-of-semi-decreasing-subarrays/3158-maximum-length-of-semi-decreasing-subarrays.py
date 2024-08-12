from sortedcontainers import SortedList
class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        for i in range(n):
            if not stack or nums[i] > nums[stack[-1]]:
                stack.append(i)
        ans = 0
        for i in range(n - 1, -1, -1):
            while len(stack) > 0 and nums[stack[-1]] > nums[i]:
                ans = max(ans, i - stack[-1] + 1)
                stack.pop(-1)
        return ans
        
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2863.Maximum%20Length%20of%20Semi-Decreasing%20Subarrays
        d = defaultdict(list)
        for i, x in enumerate(nums):
            d[x].append(i)
        ans, k = 0, inf
        for x in sorted(d, reverse=True):
            ans = max(ans, d[x][-1] - k + 1)
            k = min(k, d[x][0])
        return ans

        n = len(nums)
        hm, ans = {}, 0
        keys = SortedList()
        for i, num in enumerate(nums):
            j = n + 1
            right = bisect_right(keys, x=num)
            for k in keys[right:]:
                j = min(hm[k], j)                
            if j != n + 1:
                ans = max(ans, i - j + 1)
            if num not in hm:
                hm[num] = i
                keys.add((num, i))
        return ans
            
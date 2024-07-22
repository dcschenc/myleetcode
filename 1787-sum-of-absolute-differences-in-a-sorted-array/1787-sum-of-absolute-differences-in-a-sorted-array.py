class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1685.Sum%20of%20Absolute%20Differences%20in%20a%20Sorted%20Array
        ans = []
        s, t = sum(nums), 0
        for i, x in enumerate(nums):
            v = x * i - t + s - t - x * (len(nums) - i)
            ans.append(v)
            t += x
        return ans
        
        n = len(nums)
        d = [0]
        for a, b in pairwise(nums):
            d.append(b - a)
        pre = [0] * n
        for i in range(1, n):
            pre[i] = pre[i-1] + d[i] * i
        post = [0] * n
        for i in range(n-2, -1, -1):
            post[i] = post[i+1] + d[i + 1] * (n - 1 - i)
        
        ans = []
        for i in range(n):
            ans.append(pre[i] + post[i])
        return ans


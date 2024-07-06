class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1000-1099/1031.Maximum%20Sum%20of%20Two%20Non-Overlapping%20Subarrays
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        ans = t = 0
        i = firstLen
        while i + secondLen - 1 < n:
            t = max(t, s[i] - s[i - firstLen])
            ans = max(ans, t + s[i + secondLen] - s[i])
            i += 1
        t = 0
        i = secondLen
        while i + firstLen - 1 < n:
            t = max(t, s[i] - s[i - secondLen])
            ans = max(ans, t + s[i + firstLen] - s[i])
            i += 1
        return ans

        # n, ans = len(nums), 0
        # for i in range(n):
        #     if i + firstLen <= n:
        #         first = sum(nums[i:i + firstLen])
        #         if i >= secondLen:
        #             for j in range(i - secondLen):
        #                 second = sum(nums[j: j + secondLen])
        #                 ans = max(ans, first + second)
        #         if n - (i + firstLen) >= secondLen:
        #             for j in range(i + firstLen, n):
        #                 if j + secondLen <= n:
        #                     second = sum(nums[j: j + secondLen])
        #                     ans = max(ans, first + second)
        # return ans
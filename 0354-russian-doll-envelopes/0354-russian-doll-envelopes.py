class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # https://leetcode.com/problems/russian-doll-envelopes/editorial/
        # envelopes.sort(key=lambda x: (x[0], -x[1]))
        # # Same as 300. Longest Increasing Subsequence
        # ans = 0
        # dp = [0] * len(envelopes)
        # for _, h in envelopes:
        #     # l = 0
        #     # r = ans
        #     # while l < r:
        #     #     m = (l + r) // 2
        #     #     if dp[m] >= h:
        #     #         r = m
        #     #     else:
        #     #         l = m + 1
        #     # dp[l] = h
        #     l = bisect_left(dp[:ans], h)
        #     dp[l] = h
        #     if l == ans:
        #         ans += 1
        # return ans

        # Sort the envelopes by width in increasing order and then by height in decreasing order
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Initialize a list to store the increasing heights sequence
        dp = [envelopes[0][1]]

        # Iterate through the sorted envelopes starting from the second one
        for _, height in envelopes[1:]:
            if height > dp[-1]:  # If the current height is greater than the last in dp
                dp.append(height) # Append it as it forms an increasing sequence
            else:
                # Find the index to replace with the current height to keep sequence increasing
                index = bisect_left(dp, height)
                # Ensure the index is within range, replace the current height
                dp[index] = height
      
        # The length of dp is the length of the longest increasing subsequence
        return len(dp)
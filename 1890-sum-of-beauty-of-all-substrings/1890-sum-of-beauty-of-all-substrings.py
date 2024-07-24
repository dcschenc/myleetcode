from collections import defaultdict
class Solution:
    def beautySum(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1781.Sum%20of%20Beauty%20of%20All%20Substrings
        ans = 0
        for i in range(len(s)):
            hm = defaultdict(int)
            hm[s[i]] = 1
            for j in range(i+1, len(s)):
                hm[s[j]] += 1                
                values = hm.values()
                if max(values) - min(values) != 0:
                    ans += max(values) - min(values)
        return ans


        
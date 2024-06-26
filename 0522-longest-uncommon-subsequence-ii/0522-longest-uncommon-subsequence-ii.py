class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0500-0599/0522.Longest%20Uncommon%20Subsequence%20II
        def check(s: str, t: str):
            i = j = 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                j += 1
            return i == len(s)

        ans = -1
        for i, s in enumerate(strs):
            for j, t in enumerate(strs):
                if i != j and check(s, t):
                    break
            else:
                ans = max(ans, len(s))
        return ans
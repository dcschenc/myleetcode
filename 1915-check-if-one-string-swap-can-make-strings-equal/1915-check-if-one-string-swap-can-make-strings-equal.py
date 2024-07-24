class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1790.Check%20if%20One%20String%20Swap%20Can%20Make%20Strings%20Equal
        n = len(s1)
        idx = []
        for i in range(n):
            if s1[i] != s2[i]:
                idx.append(i)
        if len(idx) == 0 or len(idx) == 2 and s1[idx[0]] == s2[idx[1]] and s1[idx[1]] == s2[idx[0]]:
            return True
        return False
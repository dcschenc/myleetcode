class Solution:
    def countQuadruples(self, firstString: str, secondString: str) -> int:
        # If the chosen substrings are of size larger than 1, then you can remove all but the first character 
        # from both substrings, and you'll get equal substrings of size 1, with the same a but less j. 
        # Hence, it's always optimal to choose substrings of size 1.

        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1794.Count%20Pairs%20of%20Equal%20Substrings%20With%20Minimum%20Difference
        s1, s2 = firstString, secondString
        ans, count = float('inf'), 0
        hm = {}
        j = len(s2) - 1
        while j >= 0:
            if s2[j] not in hm:
                hm[s2[j]] = j
            j -= 1
        for i, c in enumerate(s1):
            if c in hm:
                if ans > (i - hm[c]):
                    ans = (i - hm[c])
                    count = 1
                elif ans == (i - hm[c]):
                    count += 1
        return count

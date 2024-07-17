class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1461.Check%20If%20a%20String%20Contains%20All%20Binary%20Codes%20of%20Size%20K
        ss = {s[i : i + k] for i in range(len(s) - k + 1)}
        return len(ss) == 1 << k

        ss = set()
        n = len(s)
        for i in range(n-k+1):
            ss.add(s[i:i+k])
        return len(ss) == 2 ** k
class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/0500-0599/0555.Split%20Concatenated%20Strings
        strs = [s[::-1] if s[::-1] > s else s for s in strs]
        ans = ''.join(strs)
        for i, s in enumerate(strs):
            t = ''.join(strs[i + 1 :]) + ''.join(strs[:i])   ## not include strs[i]
            for j in range(len(s)):
                a = s[j:]
                b = s[:j]
                ans = max(ans, a + t + b)
                ans = max(ans, b[::-1] + t + a[::-1])
        return ans
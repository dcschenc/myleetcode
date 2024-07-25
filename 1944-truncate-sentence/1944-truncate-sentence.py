class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ans = []
        i, n, cnt = 0, len(s), 0
        while i < n:
            j = i
            while j < n and s[j] != ' ':
                j += 1
            cnt += 1
            if cnt == k:
                return s[:j]
            i = j + 1
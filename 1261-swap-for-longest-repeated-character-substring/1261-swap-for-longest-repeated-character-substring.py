from collections import Counter
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1156.Swap%20For%20Longest%20Repeated%20Character%20Substring
        cnt = Counter(text)
        n = len(text)
        ans = i = 0
        while i < n:
            j = i
            while j < n and text[j] == text[i]:
                j += 1
            l = j - i
            k = j + 1
            while k < n and text[k] == text[i]:
                k += 1
            r = k - j - 1
            ans = max(ans, min(l + r + 1, cnt[text[i]]))
            i = j
        return ans
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
        return len(Counter(s).keys())
        # cnt = 0
        # i, n = 0, len(s)
        # while i < n:
        #     cnt += 1
        #     j = i + 1
        #     while j < n and s[j] == s[i]:
        #         j += 1
        #     i = j
        # return cnt

        
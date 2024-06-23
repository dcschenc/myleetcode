class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = Counter(s)
        # for c in s:
        #     hm[c] += 1
        cnt = 0
        for k, v in hm.items():
            if v%2 == 1:
                cnt += 1
        if cnt == 0:
            return len(s)
        return len(s) - cnt + 1 
class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2743.Count%20Substrings%20Without%20Repeating%20Character
        cnt = Counter()
        ans = j = 0
        for i, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[j]] -= 1
                j += 1
            ans += i - j + 1
        return ans
                
        left, n = 0, len(s)
        hm, ans = {}, 0
        for i, c in enumerate(s):
            if c in hm and left <= hm[c]:
                left = hm[c] + 1
            hm[c] = i
            ans += (i - left + 1)
        return ans
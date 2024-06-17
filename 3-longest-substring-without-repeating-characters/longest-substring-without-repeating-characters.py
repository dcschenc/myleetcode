class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        hm = {}
        for right, c in enumerate(s):
            if c not in hm or hm[c] < left:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
            else:
                if left < hm[c] + 1:
                    left = hm[c] + 1
            hm[c] = right
        return max_len

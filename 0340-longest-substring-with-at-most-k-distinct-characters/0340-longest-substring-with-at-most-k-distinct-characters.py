from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        hm = defaultdict(int)
        left = ans = 0
        for right, c in enumerate(s):
            hm[c] = right
            # if len(hm) <= k:
            #     ans = max(ans, right - left + 1)
            # else:
            if len(hm) > k:
                # hm[s[left]] -= 1
                # if hm[s[left]] == 0:
                #     del hm[s[left]]
                # left += 1
                left = min(hm.values()) + 1
                hm.pop(s[left - 1])
            ans = max(ans, right - left + 1)
        return ans


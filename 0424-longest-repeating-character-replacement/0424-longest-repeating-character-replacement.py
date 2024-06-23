class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ###### O(26n) ############
        left = mx = 0
        hm = {}
        for right in range(len(s)):
            hm[s[right]] = 1 + hm.get(s[right], 0)
            total = right - left + 1
            # max_v = sorted(hm.values(), reverse=True)[0] if hm.values() else 0
            # for _, v in hm.items():
            #     if v > max_v:
            #         max_v = v
            # max_v = max(hm.values())
            if total - max(hm.values()) <= k:
                mx = max(mx, right - left + 1)
            else:
                hm[s[left]] -= 1
                left += 1
        return mx

            

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        ans = 0
        cnt = Counter()
        for i in range(len(s) - minSize + 1):
            t = s[i : i + minSize]
            ss = set(t)
            if len(ss) <= maxLetters:
                cnt[t] += 1
                ans = max(ans, cnt[t])
        return ans

################## if ask for total number, use this ##########
        n = len(s)
        l, i, ans = 0, 0, 0
        hm = {}
        while i < n:
            if i - l  > maxSize:
                l = i - maxSize
            if s[i] not in hm and len(hm) == maxLetters:
                l = min(hm.values()) + 1
                del hm[s[min(hm.values())]]
            if i - l + 1 == minSize:
                ans += 1
            elif i - l + 1  > minSize:                    
                cur = i - l + 1 - minSize
                ans += cur    
            hm[s[i]] = i    
            i += 1            
        return ans

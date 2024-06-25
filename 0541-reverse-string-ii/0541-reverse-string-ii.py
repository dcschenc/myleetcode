class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        t = list(s)
        for i in range(0, len(t), k << 1):
            t[i : i + k] = reversed(t[i : i + k])
        return ''.join(t)
        
        s = list(s)
        i = 0
        while i < len(s):            
            if len(s) -i >= k:
                left, right = i, i+k-1
            else:
                left, right = i, len(s) - 1 
            while left < right:
                s[left], s[right] = s[right], s[left]
                left+=1
                right-=1
            i += 2*k if len(s) -i >=k else len(s)-i
        return ''.join(s)
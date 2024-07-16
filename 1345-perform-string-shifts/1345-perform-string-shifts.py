class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:        
        x = sum((b if a else -b) for a, b in shift)
        x %= len(s)
        return s[-x:] + s[:-x]
        
        for d, c in shift:
            if d == 0:
                c =  c % len(s)        
                s = s[c:] + s[:c]
            else:
                c = c % len(s)
                s = s[-c:] + s[:-c]
        return s
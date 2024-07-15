class Solution:
    def reformat(self, s: str) -> str:
        a = [c for c in s if c.islower()]
        b = [c for c in s if c.isdigit()]
        if abs(len(a) - len(b)) > 1:
            return ''
        if len(a) < len(b):
            a, b = b, a
        ans = []
        for x, y in zip(a, b):
            ans.append(x + y)
        if len(a) > len(b):
            ans.append(a[-1])
        return ''.join(ans)
        
        letters = []
        digits = []
        for c in s:
            if c.isdigit():
                digits.append(c)
            else:
                letters.append(c)

        if abs(len(digits) - len(letters)) > 1:
            return ""
            
        ans = ''
        i = 0
        while i < len(letters) and i < len(digits):
            ans += letters[i]  + digits[i]
            i += 1        
        if len(digits) > len(letters):
            ans = digits[i] + ans
        elif len(letters) > len(digits):
            ans = ans + letters[i]
        return ans

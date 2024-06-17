class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)
        while i < n and s[i] == ' ':
            i+=1
        sign = '+'
        if i<n and (s[i] == '+' or s[i] == '-'):
            sign = s[i]
            i+=1
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i+=1
        min_v = -pow(2, 31)
        max_v = pow(2, 31) - 1
        if sign == '+':
            if num > max_v:
                num = max_v
        else:            
            if num*-1 < min_v:
                num = min_v
            else:
                num = num*-1
        return num
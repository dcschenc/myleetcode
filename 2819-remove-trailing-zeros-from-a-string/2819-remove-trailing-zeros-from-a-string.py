class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip("0")
        
        n = len(num)
        i = n - 1
        ans = ''
        while i >= 0 and num[i] == '0':
            i -= 1
        return num[:i+1]

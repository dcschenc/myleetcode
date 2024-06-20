class Solution:
    def addDigits(self, num: int) -> int:
        
        while num > 9:
            res = 0
            while num > 0:
                mod = num%10
                num = num//10
                res += mod
            num = res
        return num


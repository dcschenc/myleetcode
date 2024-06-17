class Solution:
    def intToRoman(self, num: int) -> str:       
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        chars = ['M', 'CM', 'D', 'CD','C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res = ''
    
        for i, v in enumerate(numbers):
            if num == 0:
                break
            while num >= v:
                num -= v
                res += chars[i]
        return res
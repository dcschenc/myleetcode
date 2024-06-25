class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: 
            return '0'
        flag = 1
        if num < 0:
            num = abs(num)
            flag = -1
        res = ''
        while num > 0:
            mod = num %  7
            res += str(mod)
            num = num//7
        
        # res += str(num)
        return ''.join(res[::-1]) if flag == 1 else '-' + ''.join(res[::-1])
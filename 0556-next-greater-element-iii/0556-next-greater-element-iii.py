class Solution:
    def nextGreaterElement(self, n: int) -> int:
        cs = list(str(n))
        n = len(cs)
        i, j = n - 2, n - 1
        while i >= 0 and cs[i] >= cs[i + 1]:
            i -= 1
        if i < 0:
            return -1
        while cs[i] >= cs[j]:
            j -= 1
        cs[i], cs[j] = cs[j], cs[i]
        cs[i + 1 :] = cs[i + 1 :][::-1]
        ans = int(''.join(cs))
        return -1 if ans > 2**31 - 1 else ans
        
        
        def get_min_digit(j):            
            idx = -1
            for i in range(j+1, len(str_num)):
                if str_num[j] < str_num[i]:
                    idx = i                                     
            return idx

        str_num = list(str(n))
        j = len(str_num) - 2
        while j >= 0:
            idx = get_min_digit(j)
            if idx != -1:
                str_num[j], str_num[idx] = str_num[idx], str_num[j]
                # str_num[j+1:] = sorted(str_num[j+1:])  
                str_num[j+1:] = reversed(str_num[j+1:])               
                res = int(''.join(str_num))
                if res > 2 ** 31 - 1:
                    return -1
                return res
            j -= 1
        return -1


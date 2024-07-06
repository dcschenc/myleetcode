class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def is_divide(str, substr):
            if len(str)%len(substr) !=0:
                return False
            m = int(len(str)/len(substr))            
            return substr * m == str
                

        if len(str1) < len(str2):
            str1, str2 = str2, str1
        m, n = len(str1), len(str2)
        while n > 0:
            if is_divide(str1, str2[:n]) and is_divide(str2, str2[:n]):
                return str2[:n]
           
            # if n > len(str2)/2:
            #     n = len(str2)//2
            # else:
            n -= 1

        return ''


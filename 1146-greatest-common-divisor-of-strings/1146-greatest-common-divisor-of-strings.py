class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def is_divide(s, substr):
            if len(s)%len(substr) !=0:
                return False
            m = int(len(s)/len(substr))            
            return substr * m == s                

        if len(str1) < len(str2):
            str1, str2 = str2, str1
        m, n = len(str1), len(str2)
        while n > 0:
            if is_divide(str1, str2[:n]) and is_divide(str2, str2[:n]):
                return str2[:n]           
            n -= 1
        return ''


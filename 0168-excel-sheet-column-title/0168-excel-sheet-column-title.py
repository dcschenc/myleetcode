class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        base = ord('A')
        while columnNumber > 0:           
            mod = (columnNumber -1 ) % 26
            ch = chr(base + mod)
            res += ch
            columnNumber = (columnNumber-1) // 26         
       
        return res[::-1]
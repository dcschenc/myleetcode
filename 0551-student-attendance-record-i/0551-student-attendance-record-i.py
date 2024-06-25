class Solution:
    def checkRecord(self, s: str) -> bool:
        A_ctn = 0
        L_ctn = 0
        for i, c in enumerate(s):
            if c == 'A':
                A_ctn += 1
                if A_ctn == 2:
                    return False
                L_ctn = 0
            elif c == 'L': 
                L_ctn += 1
                if L_ctn == 3:
                    return False
            else:
                L_ctn = 0
            
        return True
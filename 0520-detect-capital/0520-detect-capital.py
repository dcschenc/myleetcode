class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        u_cnt = 0
        l_cnt = 0
        A_ord = ord('A')
        Z_ord = ord('Z')
        for c in word[1:]:
            if A_ord <= ord(c) <= Z_ord:
                u_cnt += 1
            else:
                l_cnt += 1
        if A_ord <= ord(word[0]) <=Z_ord:
            if u_cnt == len(word) - 1 or l_cnt == len(word) - 1:
                return True            
        else:
            if l_cnt == len(word) - 1:
                return True
        return False
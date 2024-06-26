class Solution:
    # del_ctn = False
    def validPalindrome(self, s: str) -> bool: 
        def check(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return check(i, j - 1) or check(i + 1, j)
            i, j = i + 1, j - 1
        return True
                         
        # i, j = 0, len(s) - 1
        # while i < j:
        #     if s[i] == s[j]:
        #         i += 1
        #         j -= 1
        #     else:
        #         if self.del_ctn:
        #             return False
        #         self.del_ctn = True               
        #         left, right = False, False
        #         if s[i+1] == s[j]:
        #             left = self.validPalindrome(s[i+1:j+1])
        #         if s[i] == s[j-1]:
        #             right = self.validPalindrome(s[i:j])
        #         return left or right
        # return True
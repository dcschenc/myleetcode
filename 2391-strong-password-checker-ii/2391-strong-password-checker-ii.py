class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        mask = 0
        for i, c in enumerate(password):
            if i and c == password[i - 1]:
                return False
            if c.islower():
                mask |= 1
            elif c.isupper():
                mask |= 2
            elif c.isdigit():
                mask |= 4
            else:
                mask |= 8
        return mask == 15
        
        # i, n = 0, len(password)
        # s = password
        # if n < 8: return False
        # lower = upper = digit = special = False
        # while i < n:
        #     if s[i].islower():
        #         lower = True
        #     if s[i].isupper():
        #         upper = True
        #     if s[i].isdigit():
        #         digit = True
        #     if s[i] in '!@#$%^&*()-+':
        #         special = True
        #     if i > 0 and s[i] == s[i-1]:
        #         return False
        #     i += 1
        # if lower and upper and digit and special:
        #     return True
        # return False
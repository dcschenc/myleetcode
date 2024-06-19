class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if abs(m - n) > 1:
            return False
            
        if m == n:
            for i in range(m):
                if s[i] != t[i]:
                    return s[i + 1:] == t[i + 1:]
            return False
        else:
            i, j = 0, 0
            while i < m and j < n:
                if s[i] != t[j]:
                    return s[i + 1:] == t[j:] or s[i:] == t[j + 1:]
                i += 1
                j += 1
        return True

        # m, n = len(s), len(t)
        # cnt = 0        
        # if abs(m - n) > 1:
        #     return False
        # if m == n:
        #     for i in range(m):
        #         if s[i] != t[i]:
        #             cnt += 1
        #     if cnt > 1 or cnt == 0:
        #         return False            
        # else:
        #     if m < n:
        #         i = 0
        #         for j in range(n):
        #             if i > m - 1 or s[i] != t[j]:
        #                 cnt += 1
        #                 if cnt > 1:
        #                     return False
        #             else:
        #                 i += 1                                      
        #     else:
        #         i, j = 0, 0
        #         while j < n:
        #             if s[i] != t[j]:
        #                 cnt += 1
        #                 i += 1
        #                 if cnt > 1:
        #                     return False
        #             else:
        #                 j += 1
        #                 i += 1
        # return True
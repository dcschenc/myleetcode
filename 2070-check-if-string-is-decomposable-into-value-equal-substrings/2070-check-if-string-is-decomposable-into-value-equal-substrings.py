class Solution:
    def isDecomposable(self, s: str) -> bool:
        i, n = 0, len(s)
        cnt2 = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            if (j - i) % 3 == 1:
                return False
            cnt2 += (j - i) % 3 == 2
            if cnt2 > 1:
                return False
            i = j
        return cnt2 == 1

        # cur = 0
        # prev = 0
        # len_2 = False
        # for i in range(1, len(s)):
        #     if s[i] != s[prev]:
        #         count = i - prev
        #         if count < 2:
        #             return False
        #         if count == 2:
        #             if len_2 is True:
        #                 return False
        #             len_2 = True                   
        #         if count % 3 == 0:
        #             pass
        #         elif count % 5 == 0:
        #             if len_2 is True:
        #                 return False
        #             len_2 = True
        #         else:
        #             return False
        #         prev = i
        # return len_2
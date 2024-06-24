class Solution:
    def countSegments(self, s: str) -> int:
        n = len(s)
        i = cnt = 0
        while i < n:
            if s[i] != ' ':
                j = i
                while j < n and s[j] != ' ':
                    j += 1
                i = j
                cnt += 1
            else:
                i += 1
        return cnt
        
        # n = len(s)
        # i = 0
        # cnt = 0
        # while i < n:            
        #     if s[i] == ' ':
        #         if i != 0 and s[i-1] != ' ':
        #             cnt += 1
        #     else:
        #         if i==n-1:
        #             cnt+= 1
        #     i+= 1
        # return cnt

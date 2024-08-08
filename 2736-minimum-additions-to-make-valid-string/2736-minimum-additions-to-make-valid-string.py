class Solution:
    def addMinimum(self, word: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2645.Minimum%20Additions%20to%20Make%20Valid%20String
        s = 'abc'
        ans, n = 0, len(word)
        i = j = 0
        while j < n:
            if word[j] != s[i]:
                ans += 1
            else:
                j += 1
            i = (i + 1) % 3

        if word[-1] != 'c':
            ans += 1 if word[-1] == 'b' else 2
        return ans
        
        # n = len(word)
        # ans = 0
        # i = 0
        # num_a, num_b, num_c = 0, 0, 0
        # while i < n:
        #     if word[i] == 'b':
        #         num_b += 1
        #         if i - 1 < 0 or word[i-1] != 'a':
        #             ans += 1
        #         elif i - 1 >= 0 and word[i-1] == 'a':
        #             num_a -= 1
        #     elif word[i] == 'c':
        #         if i - 1 < 0 or word[i-1] != 'b':
        #             # ans += 1     
        #             num_c += 1     
        #         elif i - 1 >= 0 and word[i-1] == 'b':
        #             num_b -= 1
        #         # else:
                    
        #     else:
        #         num_a += 1          
        #     i += 1
        # print(num_a, num_b, num_c)
        # return ans + num_a * 2 + num_b - num_c
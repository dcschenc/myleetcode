class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = ''        
        while a > 0 or b > 0:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                char = 'a' if ans[-1] == 'b' else 'b'
            else:
                char = 'a' if a > b else 'b'
            
            if char == 'a':
                ans += 'a'
                a -= 1
            else:
                ans += 'b'
                b -= 1

        return ans

        # ans = ''
        # while a > 0 and b > 0:
        #     if len(ans) > 0:
        #         if ans[-1] == 'a':
        #             if b > a:                       
        #                 ans += 'bb'
        #                 b -= 2                        
        #             else:
        #                 ans += 'b'
        #                 b -= 1
        #         elif ans[-1] == 'b':
        #             if a > b:
        #                 ans += 'aa'
        #                 a -= 2
        #             else:
        #                 ans += 'a'
        #                 a -= 1
        #     else:
        #         if a > b: 
        #             if a >= 2:                    
        #                 ans += 'aa'
        #                 a -= 2
        #             else:
        #                 ans += 'a'
        #                 a -= 1
        #         else:
        #             if b >=2:
        #                 ans += 'bb'
        #                 b -= 2
        #             else:
        #                 ans += 'b'
        #                 b -= 1
        # if a > 0:
        #     ans += 'a' * a
        # if b > 0:
        #     ans += 'b' * b
        # return ans
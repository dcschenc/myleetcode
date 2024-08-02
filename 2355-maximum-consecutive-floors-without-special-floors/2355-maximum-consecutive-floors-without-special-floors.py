class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        ans = max(special[0] - bottom, top - special[-1])
        for i in range(1, len(special)):
            ans = max(ans, special[i] - special[i - 1] - 1)
        return ans
        
        special.sort()
        ans = 0
        j, start = 0, bottom
        i, n = bottom, top
        while i <= n:
            if j < len(special):
                ans = max(ans, special[j] - start)
                start = special[j] + 1
                i = start
                j += 1
            else:
                ans = max(ans, top - start + 1)
                break
        return ans

        # for i in range(bottom, top + 1):
        #     if j < len(special) and i == special[j]:
        #         j += 1  
        #         start = i + 1   
        #     ans = max(ans, i - start + 1)
        # return ans 

        # special.sort()
        # ans = 0
        # j, start = 0, bottom
        # for i in range(bottom, top + 1):
        #     if j < len(special) and i == special[j]:
        #         j += 1  
        #         start = i + 1   
        #     ans = max(ans, i - start + 1)
        # return ans 
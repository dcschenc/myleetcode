class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        #### recursive ####
        def reverse(start, end):
            if start >= end:
                return
            s[start], s[end] = s[end], s[start]
            
            reverse(start+1, end-1)
            
        reverse(0, len(s)-1)
        
        """
        Do not return anything, modify s in-place instead.
        """
        # left, right = 0, len(s) - 1
        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -=1
        # print(s)
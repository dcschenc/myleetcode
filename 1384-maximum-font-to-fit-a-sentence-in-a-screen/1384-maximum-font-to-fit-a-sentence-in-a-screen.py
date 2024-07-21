# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:       
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1618.Maximum%20Font%20to%20Fit%20a%20Sentence%20in%20a%20Screen
        
        def can_fit(size):
            if fontInfo.getHeight(size) > h:
                return False
            return sum(fontInfo.getWidth(size, c) for c in text) <= w

        ans = -1
        left, right = 0, len(fonts) - 1
        while left <= right:
            mid = (left + right)//2            
            if can_fit(fonts[mid]): 
                left = mid + 1
            else: 
                right = mid - 1
                
        return fonts[left-1] if left else -1

       
        # ans = -1
        # for f in fonts:
        #     width = 0
        #     for ch in text:
        #         cur = fontInfo.getWidth(f, ch)                
        #         width += cur
        #     if width <= w and fontInfo.getHeight(f) <= h:
        #         ans = f
        #     else:
        #         return ans

        # return ans

        # ans = -1
        # for f in fonts:
        #     width = 0
        #     lines = 1
        #     for ch in text:
        #         cur = fontInfo.getWidth(f, ch)
        #         if width + cur > w:
        #             lines += 1
        #             width = cur
        #         else:
        #             width += cur
        #     if lines * fontInfo.getHeight(f) > h:
        #         break
        #     ans = f
        # return ans
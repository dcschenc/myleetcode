class Solution:
    def heightChecker(self, heights: List[int]) -> int:        
        # expected = heights[:]
        # expected.sort()
        expected = sorted(heights)
        count = 0 
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                count  += 1
        return count 
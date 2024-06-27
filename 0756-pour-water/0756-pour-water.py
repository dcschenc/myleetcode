class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        n = len(heights)
        for _ in range(volume):
            i = left = k
            while i - 1 >= 0 and heights[i - 1] <= heights[i]:
                if heights[i-1] < heights[i]:
                    left = i - 1
                i -= 1
            if left != k:
                heights[left] += 1
                continue

            j = right = k
            while j + 1 < n and heights[j + 1] <= heights[j]:
                if heights[j + 1] < heights[j]:
                    right = j + 1
                j += 1
            if right != k:
                heights[right] += 1
                continue
            heights[k] += 1 

        return heights

        # n = len(heights)
        # i = k - 1
        # left = 0
        # while i >= 0:
        #     if heights[i] >= heights[k]:
        #         break
        #     left += (heights[k] - heights[i])
        #     heights
        #     i -= 1
        # i = k + 1
        # right = 0
        # while i < n:
        #     if heights[i] >= heights[k]:
        #         break
        #     right += (heights[k] - heights[i])
        
            
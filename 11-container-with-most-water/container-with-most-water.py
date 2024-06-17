class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            width = right - left
            area = -1
            if height[left] < height[right]:
                area = height[left] * width
                left+=1
            else:
                area = height[right] * width
                right-=1
            if area > max_area:
                max_area = area
        return max_area
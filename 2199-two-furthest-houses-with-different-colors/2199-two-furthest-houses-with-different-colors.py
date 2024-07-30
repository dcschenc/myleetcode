class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        
        # Initializing the maximum distance to 0
        max_dist = 0
        
        # Check the distance from the first house to the last house with a different color
        for i in range(n):
            if colors[i] != colors[0]:
                max_dist = max(max_dist, i)
        
        # Check the distance from the last house to the first house with a different color
        for i in range(n):
            if colors[i] != colors[n-1]:
                max_dist = max(max_dist, n-1-i)
        
        return max_dist
        
        n, ans = len(colors), 0
        for i in range(n):
            for j in range(i+1, n):
                if colors[i] != colors[j]:
                    ans = max(ans, j - i)
        return ans
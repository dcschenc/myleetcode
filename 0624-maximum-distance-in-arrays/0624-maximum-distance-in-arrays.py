class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val, max_val = arrays[0][0], arrays[0][-1]
        max_distance = 0
        
        for i in range(1, len(arrays)):
            current_min, current_max = arrays[i][0], arrays[i][-1]
            max_distance = max(max_distance, abs(current_min - max_val), abs(current_max - min_val))
            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)

        return max_distance
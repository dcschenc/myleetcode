class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        n, m = len(encoded1), len(encoded2)
        result = []
        
        while i < n and j < m:
            value1, length1 = encoded1[i]
            value2, length2 = encoded2[j]
            
            product_value = value1 * value2
            overlap_length = min(length1, length2)
            
            # Add to result or merge with the last segment if they have the same value
            if result and result[-1][0] == product_value:
                result[-1][1] += overlap_length
            else:
                result.append([product_value, overlap_length])
            
            # Update lengths
            encoded1[i][1] -= overlap_length
            encoded2[j][1] -= overlap_length
            
            # Move to the next segment if the current one is exhausted
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1
        
        return result
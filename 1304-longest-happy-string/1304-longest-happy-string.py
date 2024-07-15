class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1405.Longest%20Happy%20String
        result, maxHeap = "", []        
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heappush(maxHeap, (count, char))
        
        while maxHeap:
            count1, char1 = heappop(maxHeap)            
            
            if len(result) > 1 and result[-1] == result[-2] == char1:
                if not maxHeap:
                    break
                count2, char2 = heappop(maxHeap)
                result += char2
                count2 += 1 # here we add 1 instead subtract coz max heap in negative
                if count2:
                    heappush(maxHeap, (count2, char2))                    
            else:
                result += char1
                count1 += 1 # here we add 1 instead subtract coz max heap in negative 
                
            if count1:
                heappush(maxHeap, (count1, char1))
                
        return result
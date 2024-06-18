from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # uniques = set(nums)
        # max_length = 0
        # while uniques:
        #     low = high = uniques.pop()            
        #     while low - 1 in uniques or high + 1 in uniques:
        #         if low - 1 in uniques:
        #             uniques.remove(low - 1)
        #             low -= 1
                
        #         if high + 1 in uniques:
        #             uniques.remove(high + 1)
        #             high += 1
        #     max_length = max(high - low + 1, max_length)

        # return max_length


        ###### O(n.k) = O(n) ########
        seen = set()
        for num in nums:
            seen.add(num)
        max_len = 0
        for i in seen:      
            start = i      
            if i - 1 not in seen:
                while i in seen:
                    i += 1           
                max_len = max(max_len, i - start)
        return max_len
        
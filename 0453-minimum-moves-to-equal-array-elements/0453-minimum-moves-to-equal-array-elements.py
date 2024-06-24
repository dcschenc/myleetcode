from collections import deque

class Solution:
    def minMoves(self, nums: List[int]) -> int:       
        # https://github.com/doocs/leetcode/tree/main/solution/0400-0499/0453.Minimum%20Moves%20to%20Equal%20Array%20Elements 
        # The algorithm leverages the fact that you can think of the problem in terms of increasing all elements to the maximum element and then count the moves needed to reach that state
        # Find the minimum element in the array.
        min_num = min(nums)    
        
        total_moves = sum(nums) - min_num * len(nums)
        
        return total_moves

        # min_num = min(nums)
        # moves = 0
        
        # for num in nums:
        #     moves += num - min_num
        
        # return moves
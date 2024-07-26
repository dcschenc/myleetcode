class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(index, current_xor):
            # When we reach the end of the array, add the current XOR total to the result
            if index == len(nums):
                return current_xor
            
            # Include the current element in the subset and calculate XOR
            include = backtrack(index + 1, current_xor ^ nums[index])
            
            # Exclude the current element from the subset
            exclude = backtrack(index + 1, current_xor)
            
            # Return the sum of XOR totals from both including and excluding the current element
            return include + exclude
        
        # Start backtracking from the first index and initial XOR total of 0
        return backtrack(0, 0)


        def dfs(idx, cur):
            if idx == n:
                ans[0] += cur
                return
            dfs(idx + 1, cur)
            dfs(idx + 1, nums[idx] ^ cur)
        n, ans = len(nums), [0]
        dfs(0, 0)
        return ans[0]
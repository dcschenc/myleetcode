class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
        return sum(map(max, zip(*nums)))
        
        m, n = len(nums), len(nums[0])
        arr = []
        for i in range(m):
            nums[i].sort(reverse=True)
            arr.append(nums[i])          
        score = 0
        for i in range(n):
            score += max([arr[j][i] for j in range(m)])
        return score

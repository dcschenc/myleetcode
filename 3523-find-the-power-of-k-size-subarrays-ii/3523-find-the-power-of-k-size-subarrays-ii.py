class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = []        
        n = len(nums)
        prev = [0] * (n)
        for i in range(1,n):
            if nums[i] == nums[i-1] + 1:
                prev[i] = prev[i-1] + 1
            else:
                prev[i] = prev[i-1]

        for i in range(k-1, n):
            if prev[i] - prev[i-k+1] == k - 1:
                ans.append(nums[i])
            else:
                ans.append(-1)
        return ans

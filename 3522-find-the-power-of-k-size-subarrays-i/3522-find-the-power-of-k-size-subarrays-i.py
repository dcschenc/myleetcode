class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/3200-3299/3254.Find%20the%20Power%20of%20K-Size%20Subarrays%20I
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

        n = len(nums)
        f = [1] * n
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                f[i] = f[i - 1] + 1
        return [nums[i] if f[i] >= k else -1 for i in range(k - 1, n)]
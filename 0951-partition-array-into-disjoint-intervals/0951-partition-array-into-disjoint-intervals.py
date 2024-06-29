class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        mx, mi = [0] * n, [float('inf')] * n
        cur = 0
        for i in range(n):
            cur = max(cur, nums[i])
            mx[i] = cur
        cur = float('inf')
        for i in range(n-1, -1, -1):
            cur = min(cur, nums[i])
            mi[i] = cur
        # print(mx, mi)        
        for i in range(n-1):
            if mx[i] <= mi[i+1]:
                return i + 1
        

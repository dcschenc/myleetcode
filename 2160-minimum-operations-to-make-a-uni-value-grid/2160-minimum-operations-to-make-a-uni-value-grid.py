class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2033.Minimum%20Operations%20to%20Make%20a%20Uni-Value%20Grid
        nums = []
        mod = grid[0][0] % x
        for row in grid:
            for v in row:
                if v % x != mod:
                    return -1
                nums.append(v)
        nums.sort()
        mid = nums[len(nums) >> 1]
        return sum(abs(v - mid) // x for v in nums)

        # arr = [row[j] for j in range(len(grid[0])) for row in grid]
        # arr.sort()
        # mod = arr[0] % x
        # for num in arr:
        #     if num % x != mod:
        #         return -1
        # n = len(arr)
        # mid = arr[n//2]       
        # for num in arr:
        #     ans += abs(num - mid) // x
        # return ans
       
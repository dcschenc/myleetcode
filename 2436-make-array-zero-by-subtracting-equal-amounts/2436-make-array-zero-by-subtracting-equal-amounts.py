class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2357.Make%20Array%20Zero%20by%20Subtracting%20Equal%20Amounts
        return len({x for x in nums if x})

        # nums.sort()
        # steps = 0
        # while any(num != 0 for num in nums):
        #     mi = min([v for v in nums if v >0])
        #     for i in range(n):
        #         if nums[i] > 0:
        #             nums[i] -= mi
        #     steps += 1
        # return steps
        
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        for i in range(n):
            if i % 2 == 0:
                res += nums[i]
        return res

    # Create an array to store counts of each number in the input list.
        # num_counts = [0] * 20001  # Range of values from -10,000 to 10,000
        
        # # Populate the count array.
        # for num in nums:
        #     num_counts[num + 10000] += 1
        
        # result = 0
        # take = True
        
        # for i in range(20001):
        #     while num_counts[i] > 0:
        #         if take:
        #             result += i - 10000
        #         take = not take
        #         num_counts[i] -= 1
        
        # return result

       
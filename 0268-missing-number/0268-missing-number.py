class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0200-0299/0268.Missing%20Number
        total_xor, n = 0, len(nums)
        for i, num in enumerate(nums, 1):
            total_xor ^= (i)
            total_xor ^= num
            
        # total_xor ^= n
        return total_xor

        return reduce(xor, (i ^ v for i, v in enumerate(nums, 1)))


        ########### method 1 ###########
        n = len(nums)
        i = 0
        while i < n:       
            j = nums[i]    
            if nums[i] < n and nums[i] != i:                
                nums[j], nums[i] = nums[i], nums[j]
            else:
                i+=1
        i = 0
        while i < n:            
            if nums[i] != i:
                return i
            i+=1
        return n

        ########### method 2 ##########
        n = len(nums)
        total_xor = 0

        # XOR all numbers from 0 to n
        for i in range(n + 1):
            total_xor ^= i

        # XOR all numbers in the array
        for num in nums:
            total_xor ^= num

        return total_xor

        ######## method 3 ##########
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

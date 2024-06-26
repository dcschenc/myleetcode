from collections import defaultdict
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # xor_result = 0
        # # First pass: calculate the XOR of all indices and the elements in nums
        # for index, value in enumerate(nums, 1):
        #     xor_result ^= index ^ value

        # # Obtain the rightmost set bit (least significant bit)
        # # This will serve as a mask for segregating numbers
        # rightmost_set_bit = xor_result & -xor_result

        # # We will use `number_a` to find one of the numbers by segregating into two buckets
        # # The rightmost set bit will allow us to xor numbers into two groups
        # # One group where the bit is set and another where it's not
        # number_a = 0
        # for index, value in enumerate(nums, 1):
        #     if index & rightmost_set_bit:
        #         number_a ^= index
        #     if value & rightmost_set_bit:
        #         number_a ^= value
      
        # # `number_b` is the other number we need to find
        # number_b = xor_result ^ number_a

        # # Check if `number_a` is the duplicated number or the missing number
        # # If `number_a` is found in nums, it is the duplicated one
        # for value in nums:
        #     if value == number_a:
        #         return [number_a, number_b]
      
        # # If `number_a` is not in nums, it's the missing number and `number_b` is the duplicate
        # return [number_b, number_a]


        n = len(nums)
        seen = set()
        for num in nums:
            if num in seen:
                duplicate = num
                break
            seen.add(num)
        sum1 = n * (n + 1) //2 
        sum2 = sum(nums)
        missing = duplicate - (sum2 - sum1)
        return [duplicate, missing]

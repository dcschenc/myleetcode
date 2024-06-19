# from collections import d
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Custom comparison function for sorting
        def compare(x, y):
            return int(x + y) - int(y + x)

        # Convert integers to strings
        nums = list(map(str, nums))
        # Sort the numbers using the custom comparison function
        nums = sorted(nums, key=cmp_to_key(compare), reverse=True)
        # Join the sorted numbers to form the largest number
        largest = ''.join(nums)

        # Handle leading zeros
        return str(int(largest))

        # def compare(x, y):
        #     if int(str(x) + str(y)) == int(str(y) + str(x)):
        #         return 0
        #     elif int(str(x) + str(y)) > int(str(y) + str(x)):
        #         return -1
        #     else:
        #         return 1   
            

        # res = ''
        # hm = {}
        # for num in nums:
        #     k = str(num)[0]
        #     if k in hm:
        #         hm[k].append(num)
        #     else:
        #         hm[k] = [num]
        # for k in range(9, -1, -1):
        #     k = str(k)
        #     if k in hm:
        #         arr = hm[k]
        #         if len(arr) == 1:
        #             if res != '0':
        #                 res += str(arr[0])                
        #         else:
        #             arr = sorted(arr, key=cmp_to_key(compare))
        #             for a in arr:
        #                 if res != '0':
        #                     res += str(a)

        # return res
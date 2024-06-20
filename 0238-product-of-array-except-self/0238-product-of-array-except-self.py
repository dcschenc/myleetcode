class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result

        # return result        
        # length = len(nums)
        # left, right = [0] * length, [0] * length
        # left[0]=nums[0]
        # right[length-1] = nums[length - 1]
        # i = 1
        # while i < length:
        #     left[i] = left[i-1]*nums[i]
        #     right[length-i-1] = nums[length-i-1]*right[length-i]
        #     i+=1
        # # for i in range(length):
        # #     if i == 0:
        # #         left.append(nums[0])
        # #     else:
        # #         left.append(left[i-1]*nums[i])

        # # for i in range(length-1, -1, -1):
        # #     if i == len(nums) - 1:
        # #         right.append(nums[length - 1])
        # #     else:
        # #         right.append(nums[i]*right[-1])        
        # # print(left)
        # # right.reverse()
        # # print(right)
        
        # res = [0] * length
        # res[0] = right[1]
        # res[length-1] = left[length-2]
        # for i in range(1, length-1):
           
        #     res[i] = left[i-1] * right[i+1]
        # # print(res)
        # return res
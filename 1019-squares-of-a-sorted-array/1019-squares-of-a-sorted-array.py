class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1

        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]

            if left_square > right_square:
                result[pos] = left_square
                left += 1
            else:
                result[pos] = right_square
                right -= 1

            pos -= 1

        return result

        # mid = 0
        # res = []        
        # length = len(nums)
        # # if length == 1:
        #     # return [nums[0] * nums[0]]
        # i, j = 0, 0
        # for i in range(length):
        #     if nums[i] >=0:               
        #         break
        #     j = i + 1
            
       
        # if j == length:
        #     i = length - 1
        # else:
        #     i = i-1
        # # print(i, j, length)
        
        # while i >=0 and j < length:
        #     left, right = nums[i]*nums[i], nums[j]*nums[j]
        #     if left <= right:
        #         res.append(left)
        #         i -= 1
        #     else:
        #         res.append(right)
        #         j += 1
                
        # while i >= 0:
        #     res.append(nums[i] * nums[i])
        #     i -= 1
        # while j < length:
        #     res.append(nums[j] * nums[j])
        #     j += 1
        # return res
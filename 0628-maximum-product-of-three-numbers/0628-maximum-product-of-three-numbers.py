class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0600-0699/0628.Maximum%20Product%20of%20Three%20Numbers
        nums.sort()
        a = nums[-1] * nums[-2] * nums[-3]
        b = nums[-1] * nums[0] * nums[1]
        return max(a, b)

        # nums.sort()
        # n = len(nums)
        # i = 0
        # while i < n:
        #     if nums[i] >= 0:
        #         break
        #     i += 1
        # if i == 0:
        #     return nums[-3]*nums[-2]*nums[-1]
        # if i == n:
        #     return nums[-3]*nums[-2]*nums[-1]
        # if nums[0]*nums[1] > nums[-3]*nums[-2]:
        #     return nums[0]*nums[1]*nums[-1]
        # else:
        #     return nums[-3]*nums[-2]*nums[-1]
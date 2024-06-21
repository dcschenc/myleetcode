class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = math.inf
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:  
                second = num
            else: 
                return True
        return False

        # n = len(nums)
        # p1, p2 = 0, 0
        # count = 0
        # new = True
        # n1, n2 = -1, -1
        # for i in range(1, n):
        #     if nums[i] == nums[i-1] and p2 == i-1:
        #         p2 = i
        #         # if i == 1:
        #         #     p1 = p2
        #         # continue
        #     elif nums[i] == nums[p2]:
        #         p2 = i
        #         if i == 1:
        #             p1 = p2
        #     elif nums[i] < nums[p2]:
        #         if n1 == -1:
        #             n1 = i
        #             if nums[n1] >= nums[p1]:
        #                 p2 = i
        #         elif nums[i] > nums[n1]:
        #             n2 = i
        #             p1 = n1
        #             p2 = n2
        #             n1 = -1
        #     elif p1 != p2:
        #         return True
        #     if nums[i] >= nums[p2] and p1 == p2:
        #         p2 = i
        # return False

        # for i in range(1,n):
        #     if nums[i] <= nums[max_i]:
        #         print(i, nums[i], n1, n2)
        #         n1 = i
        #         if n1 != -1:
        #             min_i = n1
        #             max_i = n2
        #             # n1 = -1
        #     elif min_i != max_i:
        #         return True
        #     if nums[i] >= nums[max_i] and min_i == max_i:
        #         max_i = i
        #     if n1 != -1 and nums[i] >= nums[n1]:
        #         n2 = i
        #         # min_i = n1
        #         # max_i = n2
        # return False
            
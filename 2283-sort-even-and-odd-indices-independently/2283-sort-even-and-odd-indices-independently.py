class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2164.Sort%20Even%20and%20Odd%20Indices%20Independently
        a = sorted(nums[::2])
        b = sorted(nums[1::2], reverse=True)
        nums[::2] = a
        nums[1::2] = b
        return nums
        
        # odd, even = [], []
        # for i, num in enumerate(nums):
        #     if i % 2 == 0:
        #         even.append(nums[i])
        #     else:
        #         odd.append(nums[i])

        # odd.sort(reverse=True)
        # even.sort()
        # i, j = 0, 0
        # m, n = len(odd), len(even)
        # ans = []
        # while i < m and j < n: 
        #     ans.append(even[i])
        #     ans.append(odd[i])
        #     i += 1
        #     j += 1
        # if i < m:
        #     ans.extend(odd[i:])
        # if j < n:
        #     ans.extend(even[j:])
        # return ans
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd, even = [], []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        ans, l, r = [], 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                ans.append(even[r])
                r += 1
            else:
                ans.append(odd[l])
                l += 1
        return ans
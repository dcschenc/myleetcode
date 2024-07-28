class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counter = Counter()
        ans = 0
        for num in nums:
            ans += counter[num - k] + counter[num + k]
            counter[num] += 1
        return ans

        # n, ans = len(nums), 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if abs(nums[i] - nums[j]) == k:
        #             ans += 1
        # return ans
        

        # nums.sort()
        # n = len(nums)
        # i, j = 0, len(nums) - 1
        # ans = 0
        # print(nums)
        # while i < j:
        #     diff = nums[j] - nums[i]
        #     if diff == k:
        #         k = i + 1
        #         while k < n and nums[i] == nums[k-1]:
        #             k += 1
        #         m = j - 1
        #         while m > 0 and nums[m] == nums[m+1]:
        #             m -= 1
        #         # print(k, m)
        #         ans += (k - i - 1) * (j - m )
        #         i = k
        #         j = m
        #     elif diff > k:
        #         i += 1
        #     else:
        #         j -= 1
        # return ans
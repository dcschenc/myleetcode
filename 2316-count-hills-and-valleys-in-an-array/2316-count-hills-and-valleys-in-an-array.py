class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = j = 0
        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            if nums[i] > nums[j] and nums[i] > nums[i + 1]:
                ans += 1
            if nums[i] < nums[j] and nums[i] < nums[i + 1]:
                ans += 1
            j = i
        return ans

        # arr = [nums[0]]
        # for v in nums[1:]:
        #     if v != arr[-1]:
        #         arr.append(v)
        # return sum(
        #     (arr[i] < arr[i - 1]) == (arr[i] < arr[i + 1])
        #     for i in range(1, len(arr) - 1)
        # )
        
        # cnt = 0
        # i, n = 1, len(nums)
        # hill_valleys = [0] * n
        # while i < n - 1:
        #     l = i - 1
        #     while l >= 0 and nums[l] == nums[i]:
        #         l -= 1
        #     hill, valley = 0, 0
        #     if l >= 0:
        #         if nums[i] > nums[l]:
        #             hill += 1
        #         else:
        #             valley += 1
        #     r = i + 1
        #     while r <= n-1 and nums[r] == nums[i]:
        #         r += 1
        #     if r <= n-1:
        #         if nums[i] > nums[r]:
        #             hill += 1
        #         else:
        #             valley += 1
        #     if hill == 2:
        #         hill_valleys[i] = 'h'
        #     if valley == 2:
        #         hill_valleys[i] = 'v'
        #     i += 1
        
        # ans = 0
        # for i, c in enumerate(hill_valleys):
        #     if (c == 'h' or c == 'v') and hill_valleys[i-1] != c:
        #         ans += 1
        # return ans

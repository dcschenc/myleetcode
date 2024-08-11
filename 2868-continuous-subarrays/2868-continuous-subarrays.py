class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        left = 0
        res = 0
        for right, num in enumerate(nums):
            cnt[num] += 1
            while max(cnt) - min(cnt) > 2:
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            res += right - left + 1
        return res

        ans = i = 0
        sl = SortedList()
        for x in nums:
            sl.add(x)
            while sl[-1] - sl[0] > 2:
                sl.remove(nums[i])
                i += 1
            ans += len(sl)
        return ans

        # n = len(nums)
        # i, l, ans = 0, -1, 0
        # mx_pos, mi_pos = 0, 0
        # while i < n:
        #     if nums[mi] <= nums[i] <= nums[mx]:
        #         ans += i - l
        #     elif nums[i] < nums[mi]:
        #         if nums[mx] - nums[i] <= 2:
        #             ans += i - l
        #             mi = i 

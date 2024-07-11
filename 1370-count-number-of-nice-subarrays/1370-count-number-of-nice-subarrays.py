class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1200-1299/1248.Count%20Number%20of%20Nice%20Subarrays
        ### prefix sum ###
        cnt = Counter({0: 1})
        ans = cur = 0
        for num in nums:
            if num % 2 == 1:
                cur += 1
            ans += cnt[cur - k]
            cnt[cur] += 1
        return ans

        # count = 0
        # left = 0
        # nice_subarrays = 0
        # current_count = 0
        # # Iterate ove the whole array for counting the length of the nice subarrays

        # for right in range(len(nums)):
        #     # Checking if the number is a number is odd and reinitializing the count for next iteration counting
        #     if nums[right]%2 != 0:
        #         current_count += 1
        #         count = 0
        #     if current_count == k:
        #         # check if the number at left is even and increment left while True since this doesn't effect our current_counter
        #         while left < len(nums) and nums[left] % 2 == 0:
        #             count+=1
        #             left += 1
        #         # if the number is odd increment the count by one
        #         count += 1
        #         current_count -= 1
        #         left += 1
        #     nice_subarrays += count
        # return nice_subarrays


        # n = len(nums)
        # left, right, cnt, ans = 0, 0, 0, 0
        # idx = []
        # for i in range(n):
        #     if nums[i] % 2 == 1:
        #         if len(idx) == k + 1:                
        #             ans += (idx[1] - idx[0] + 1) * (i - idx[-1] + 1)
        #             idx = idx[1:]
        #         if i == n - 1 and len(idx) == k:
        #             ans += (idx[0] + 1) * (i - idx[-1] + 1)
        #         idx.append(i)

        # if nums[n-1] % 2 == 0:
        #     if len(idx) == k:
        #         ans += (idx[0] + 1) * (i - idx[-1] + 1)
        #     elif len(idx) > k:
        #         ans += (idx[1] - idx[0] + 1) * (i - idx[-1] + 1)
        # return ans
                    
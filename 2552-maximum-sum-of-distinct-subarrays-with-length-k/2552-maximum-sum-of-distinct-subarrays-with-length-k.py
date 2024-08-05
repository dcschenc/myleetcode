class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2461.Maximum%20Sum%20of%20Distinct%20Subarrays%20With%20Length%20K  
        cnt = Counter(nums[:k])
        s = sum(nums[:k])
        ans = s if len(cnt) == k else 0
        for i in range(k, len(nums)):
            cnt[nums[i]] += 1
            cnt[nums[i - k]] -= 1
            if cnt[nums[i - k]] == 0:
                cnt.pop(nums[i - k])
            s += nums[i] - nums[i - k]
            if len(cnt) == k:
                ans = max(ans, s)
        return ans

        # presum, n = [0], len(nums)
        # for i in range(n):
        #     presum.append(presum[-1] + nums[i])
        # ans, cnt, hm = 0, 0, {}
        # i, start = 0, 0
        # while i < n:
        #     if nums[i] not in hm:                
        #         cnt += 1                
        #     else:                
        #         j = hm[nums[i]]
        #         if j >= start:
        #             start = j + 1
        #         cnt = i - start + 1
        #     hm[nums[i]] = i
        #     if cnt >= k:
        #         ans = max(ans, presum[i + 1] - presum[i + 1 - k])
        #     i += 1

        # return ans
            

  
        
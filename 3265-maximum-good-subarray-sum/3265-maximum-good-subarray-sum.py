class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = -inf
        prefix = {nums[0]: 0}
        s, n = 0, len(nums)
        for i, x in enumerate(nums):
            s += x
            if x - k in prefix:
                ans = max(ans, s - prefix[x - k])
            if x + k in prefix:
                ans = max(ans, s - prefix[x + k])
            if i + 1 < n and (nums[i + 1] not in prefix or prefix[nums[i + 1]] > s):
                prefix[nums[i + 1]] = s
        return 0 if ans == -inf else ans


        hm = defaultdict(list)
        n, ans = len(nums), float('-inf')
        presum = [0]
        for i in range(n):
            x = nums[i]
            hm[x + k].append(i)
            hm[x - k].append(i)
            presum.append(presum[-1] + nums[i])
        for i in range(n):
            candidates = hm[nums[i]]
            for j in candidates:
                if nums[i] == nums[j]: continue
                if j > i:
                    ans = max(ans, presum[j + 1] - presum[i])
                elif j < i:
                    ans = max(ans, presum[i + 1] - presum[j])

        return ans if ans != float('-inf') else 0
            

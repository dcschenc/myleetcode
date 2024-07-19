class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1546.Maximum%20Number%20of%20Non-Overlapping%20Subarrays%20With%20Sum%20Equals%20Target
        # hm = defaultdict(list)
        hm = set()
        ans = 0
        pre = enumerate(accumulate(nums, initial = 0))        
        for i, s in pre:
            comp = s - target
            if comp in hm:
                ans += 1
                hm.clear()
            # hm[num] = i
            hm.add(s)
        return ans

        # n = len(nums)
        # pre = [0] * (n + 1)
        # for i in range(1, n+1):
        #     pre[i] = pre[i - 1] + nums[i-1]        

        # cur, ans = 0, 0
        # for i in range(1, n + 1):            
        #     if cur == target:
        #         ans += 1
        #         cur = 0
        # return ans
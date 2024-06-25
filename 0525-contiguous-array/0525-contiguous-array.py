class Solution:
    def findMaxLength(self, nums: List[int]) -> int:   
        # https://github.com/doocs/leetcode/tree/main/solution/0500-0599/0525.Contiguous%20Array
        n = len(nums)
        hm = {0:-1}
        presum = 0
        max_len = 0
        for i in range(n):
            if nums[i] == 0:
                presum -= 1
            else:
                presum += 1
            if presum in hm:
                max_len = max(max_len, i - hm[presum])
            else:
                hm[presum] = i
        return max_len
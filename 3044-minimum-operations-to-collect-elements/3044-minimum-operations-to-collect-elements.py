class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # is_added = [False] * k
        # count = 0
        # n = len(nums)
        # for i in range(n - 1, -1, -1):
        #     if nums[i] > k or is_added[nums[i] - 1]:
        #         continue
        #     is_added[nums[i] - 1] = True
        #     count += 1
        #     if count == k:
        #         return n - i
                
        s = set()
        steps = 0
        for i in range(len(nums) - 1, -1, -1):
            steps += 1
            if nums[i] <= k and nums[i] not in s:
                s.add(nums[i])
                if len(s) == k:
                    break
        return steps
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        steps = 0
        while len(nums) >= 2 and nums[0] < k:
            v1, v2 = heappop(nums), heappop(nums)
            v = min(v1, v2) * 2 + max(v1, v2)
            heappush(nums, v)
            steps += 1
        return steps

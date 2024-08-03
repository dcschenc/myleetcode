class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pair = n * (n-1)//2
        hm = defaultdict(int)
        cnt = 0
        for i, num in enumerate(nums):
            key = nums[i] - i 
            hm[key] += 1
        for k, v in hm.items():           
            cnt += v * (v-1)//2
        return total_pair - cnt
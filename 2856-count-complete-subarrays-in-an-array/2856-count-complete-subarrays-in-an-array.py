class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        hm = set(nums)
        cnt = 0
        for i in range(n):
            cur = set()            
            for j in range(i, n):
                cur.add(nums[j])
                if cur == hm:
                    cnt += n - j
                    break
        return cnt

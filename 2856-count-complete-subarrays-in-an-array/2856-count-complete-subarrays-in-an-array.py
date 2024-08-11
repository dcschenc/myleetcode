class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        cnt = len(set(nums))
        ans, n = 0, len(nums)
        for i in range(n):
            s = set()
            for x in nums[i:]:
                s.add(x)
                if len(s) == cnt:
                    ans += 1
        return ans
        
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

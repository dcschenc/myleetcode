class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total = len(set(nums))
        left, result, n = 0, 0, len(nums)
        result = 0
        cur = Counter()
        
        for right in range(n):
            # Expand the window by including nums[right]
            cur[nums[right]] += 1
            
            # While the window contains all unique elements
            while len(cur) == total:
                # Count all subarrays from left to right
                result += (n - right)
                
                # Move the left boundary of the window to shrink it
                cur[nums[left]] -= 1
                if cur[nums[left]] == 0:
                    del cur[nums[left]]
                left += 1
        
        return result
        

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

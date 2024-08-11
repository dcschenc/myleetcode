class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique_elements = set(nums)
        total_unique = len(unique_elements)
        n = len(nums)
        left = 0
        result = 0
        current_window = {}
        
        for right in range(n):
            # Expand the window by including nums[right]
            if nums[right] in current_window:
                current_window[nums[right]] += 1
            else:
                current_window[nums[right]] = 1
            
            # While the window contains all unique elements
            while len(current_window) == total_unique:
                # Count all subarrays from left to right
                result += (n - right)
                
                # Move the left boundary of the window to shrink it
                current_window[nums[left]] -= 1
                if current_window[nums[left]] == 0:
                    del current_window[nums[left]]
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

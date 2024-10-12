class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        # ans = []
        # n = len(nums)
        # for i in range(n):
        #     if any(abs(i - j) <= k and nums[j] == key for j in range(n)):
        #         ans.append(i)
        # return ans

        result = set()
        
        # Step 1: Find all indices where nums[j] == key
        key_indices = [j for j in range(len(nums)) if nums[j] == key]
        
        # Step 2: For each key index, add all indices within distance k to the result set
        for j in key_indices:
            # Add indices from max(0, j - k) to min(len(nums) - 1, j + k)
            for i in range(max(0, j - k), min(len(nums), j + k + 1)):
                result.add(i)
        
        # Step 3: Return sorted list of unique indices
        return sorted(result)
        
        n = len(nums)
        target = [i for i, num in enumerate(nums) if num == key]        
        ans = []
        for i , num in enumerate(nums):
            idx = bisect_left(target, i)
            if idx > 0 and target[idx-1] + k >= i or idx < len(target) and target[idx] - i <= k:
                ans.append(i)
        return ans
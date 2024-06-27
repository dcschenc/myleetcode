class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess):
            left = count = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > guess:
                    left += 1
                count += right - left
            return count

        nums.sort()        
        low, high = 0, nums[-1] - nums[0]
        while low <= high:
            mid = (low + high) // 2
            count = possible(mid)
            #### too many pairs are less than mid (distance), need to decrease the distance
            if count >= k:
                high = mid - 1
            else:
                low = mid + 1
            # print(low, mid, high)
            
        return high + 1        
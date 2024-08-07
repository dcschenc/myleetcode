class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2592.Maximize%20Greatness%20of%20an%20Array
        nums.sort()
        ans, n = 0, len(nums)
        l, r = 0, 1
        while l < n and r < n:
            if nums[l] < nums[r]:
                ans += 1
                l += 1
            r += 1            
        return ans

        # counter = Counter(nums)
        # ans = 0
        # keys = counter.keys()
        # keys.sort()
        # for k in keys:

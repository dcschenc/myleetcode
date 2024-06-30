class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                d = nums[i - 1] - nums[i] + 1
                nums[i] += d
                ans += d
        return ans

        # max_val = max(nums)
        # count = collections.Counter(nums)
        # taken = []        
        # moves = 0
        # for x in range(len(nums) + max_val):
        #     if count[x] >= 2:
        #         taken.extend([x] * (count[x] - 1))
        #     elif taken and count[x] == 0:
        #         moves += x - taken.pop()                
        # return moves

        # hash_set = set(nums)
        # counter = Counter(nums)
        # for num in nums:
        #     if counter[num] > 1

        # nums.sort()
        # n = len(nums)
        # # gap = nums[-1] - nums[0]
        # for 
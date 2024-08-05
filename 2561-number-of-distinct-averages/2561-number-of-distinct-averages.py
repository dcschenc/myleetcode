class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        # counter = Counter()
        ss = set()
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            # counter[(nums[i] + nums[j]) / 2] += 1
            ss.add((nums[i] + nums[j]) / 2)
            i += 1
            j -= 1
        return len(ss)
        # return len(counter)
        
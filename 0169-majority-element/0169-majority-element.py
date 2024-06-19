class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # dict_ = defaultdict(int)
        # for val in nums:
        #     dict_[val] += 1
        # for key, val in dict_.items():
        #     if val > len(nums)/2:
        #         return key

        # Moore's Voting Algorithm
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

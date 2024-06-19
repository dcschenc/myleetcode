class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
            # if val not in hm:
            #     hm[val] = i
            # else:
            #     if i - hm[val] <= k:
            #         return True
            #     else:
            #         hm[val] = i
        return False
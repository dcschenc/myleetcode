
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hm = Counter(nums)
        cnt = 0
        # for num in nums:
        #     if num in hm:
        #         hm[num] += 1
        #     else:
        #         hm[num] = 1
        for num in hm:
            if k > 0 and num + k in hm:
                cnt += 1
            if k == 0 and hm[num] > 1:
                cnt += 1
        return cnt

        nums = sorted(nums)

        left = 0
        right = 1

        result = 0

        while (left < len(nums) and right < len(nums)):
            if (left == right or nums[right] - nums[left] < k):
                # List item 1 in the text
                right += 1
            elif nums[right] - nums[left] > k:
                # List item 2 in the text
                left += 1
            else:
                # List item 3 in the text
                left += 1
                result += 1
                while (left < len(nums) and nums[left] == nums[left - 1]):
                    left += 1

        return result
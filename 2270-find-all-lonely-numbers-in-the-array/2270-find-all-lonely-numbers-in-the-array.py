from collections import defaultdict
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2150.Find%20All%20Lonely%20Numbers%20in%20the%20Array
        cnt = Counter(nums)
        return [
            x for x, v in cnt.items() if v == 1 and cnt[x - 1] == 0 and cnt[x + 1] == 0
        ]

        hm = defaultdict(list)
        for i, num in enumerate(nums):
            hm[num].append(i)        
        ans = []
        num_set = set(hm.keys())
        for num in nums:
            if len(hm[num]) > 1 or num + 1 in num_set or num - 1 in num_set:
                continue
            ans.append(num)
        return ans


        # nums.sort()
        # ans = []
        # if len(nums) == 1 or nums[0] != nums[1] and nums[0] + 1 != nums[1]:
        #     ans.append(nums[0])
        # # print(nums)
        # for i in range(1, len(nums)-1):
        #     if nums[i] != nums[i-1] and nums[i] != nums[i-1] + 1 and nums[i] != nums[i+1] and nums[i] != nums[i+1] - 1:
        #         ans.append(nums[i])
        
        # if len(nums) != 1 and nums[-1] != nums[-2] + 1 and nums[-1] != nums[-2]:
        #     ans.append(nums[-1])
        # return ans

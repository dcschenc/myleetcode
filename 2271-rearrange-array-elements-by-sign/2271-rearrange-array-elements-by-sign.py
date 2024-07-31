class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2149.Rearrange%20Array%20Elements%20by%20Sign
        ans = [0] * len(nums)
        i, j = 0, 1
        for x in nums:
            if x > 0:
                ans[i] = x
                i += 2
            else:
                ans[j] = x
                j += 2
        return ans

        # pos, neg = [], []
        # for n in nums:
        #     if n > 0:
        #         pos.append(n)
        #     else:
        #         neg.append(n)
        # # print(pos, neg)
        # ans = []
        # i = 0
        # while i < len(nums):
        #     if i % 2 == 0:
        #         ans.append(pos[i//2])
        #     else:
        #         ans.append(neg[i//2])
        #     i += 1
        # return ans
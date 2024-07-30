class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2098.Subsequence%20of%20Size%20K%20With%20the%20Largest%20Even%20Sum
        nums.sort(reverse = True)
        n = len(nums)
        topkSum = sum(nums[:k])
        if topkSum % 2 == 0: return topkSum

        minOdd = minEven = float('inf')

        for i in range(k):
            if nums[i] % 2 == 1:
                minOdd = min(minOdd, nums[i])
            else:
                minEven = min(minEven, nums[i])

        ret = -1
        for i in range(k,n):
            if nums[i] % 2 == 1 and minEven != float('inf'):
                ret = max(ret, topkSum + nums[i] - minEven)
            if nums[i] % 2 == 0 and minOdd != float('inf'):
                ret = max(ret, topkSum + nums[i] - minOdd)

        return ret
class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2964.Number%20of%20Divisible%20Triplet%20Sums
        cnt = defaultdict(int)
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                k = (d - (nums[i] + nums[j]) % d) % d
                if k in cnt:
                    ans += cnt[k]
            cnt[nums[i] % d] += 1
        return ans

        # n = len(nums)
        # ans = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             if (nums[i] + nums[j] + nums[k]) % d == 0:
        #                 ans += 1
        # return ans
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2870.Minimum%20Number%20of%20Operations%20to%20Make%20Array%20Empty
        counter = Counter(nums)
        ans = 0
        for v in counter.values():
            if v == 1:
                return -1
            # ans += (v + 2) // 3
            ans += math.ceil(v / 3)
        return ans

        # ans = 0
        # print(counter)
        # for k, v in counter.items():
        #     if v % 3 == 0:
        #         ans += v // 3
        #     elif v % 5 == 0:
        #         ans += 2 * (v // 5)
        #     elif v % 2 == 0:
        #         ans += v // 2
        #     else:
        #         if v > 3 and (v - 3) % 2 == 0:
        #             ans += 1
        #             ans += (v - 3) // 2
        #         else:
        #             return -1
        # return ans

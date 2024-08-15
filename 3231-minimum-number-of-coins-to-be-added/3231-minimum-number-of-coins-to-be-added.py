class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2952.Minimum%20Number%20of%20Coins%20to%20be%20Added
        coins.sort()
        num = 0
        additions = 0
        i = 0
        while num < target:
            if i < len(coins) and coins[i] <= num + 1:
                num += coins[i]
                i += 1
            else:
                num += num + 1
                additions += 1

        return additions

        # coins.sort()
        # s = 1
        # ans = i = 0
        # while s <= target:
        #     if i < len(coins) and coins[i] <= s:
        #         s += coins[i]
        #         i += 1
        #     else:
        #         s <<= 1
        #         ans += 1
        # return ans

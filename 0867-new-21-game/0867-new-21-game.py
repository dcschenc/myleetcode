class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if not k:
            return 1

        # dp[i] = probability of getting i points at any point in the game
        dp = [0.0] * (n+1)
        dp[0] = 1

        # cumulative probability of all states that can reach i — starts at 1 bc dp[0]=1
        # represents the sum of a sliding window
        prob_of_previous_states = 1

        for i in range(1, n+1):
            # prob of drawing num = sum_allprevs(prob of reaching prev state + 1/maxpts)
            # = prob of all prev states * 1/maxPts
            dp[i] = prob_of_previous_states / maxPts

            # if A continues drawing, we add the current entry to the cumulative sum
            if i < k:
                prob_of_previous_states += dp[i]

            # If A continues drawing, we subtract the out of range entry from the cumulative sum
            # This is because that entry cannot reach the next value
            if 0 <= i - maxPts < k:
                prob_of_previous_states -= dp[i - maxPts]


        # we want the probability that the final score is n or fewer
        # because she stops drawing at k, this is equivalent to the probability that the final score is in [k, n]
        # in other words, we want sum(dp[i]) | k ≤ i ≤ n
        # dp is already upper bounded by n, so sum(dp[k:]) is our answer
        return sum(dp[k:])

        # https://github.com/doocs/leetcode/tree/main/solution/0800-0899/0837.New%2021%20Game
        @cache
        def dfs(i: int) -> float:
            if i >= k:
                return int(i <= n)
            if i == k - 1:
                return min(n - k + 1, maxPts) / maxPts
            return dfs(i + 1) + (dfs(i + 1) - dfs(i + maxPts + 1)) / maxPts

        return dfs(0)
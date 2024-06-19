class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [0] * n
        for i, r in enumerate(ratings):
            if i == 0:
                candy[i] = 1
            elif ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
            else:
                candy[i] = 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                if candy[i] <= candy[i+1]:
                    candy[i] = candy[i+1] + 1

        return sum(candy)


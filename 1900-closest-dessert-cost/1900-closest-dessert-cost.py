class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1774.Closest%20Dessert%20Cost
        @cache
        def solve(value, j=0):
            if j == len(toppingCosts):
                return value

            # Pruning makes this really fast!
            if value > target:
                return value

            return min( 
                        solve(value + 2 * toppingCosts[j], j + 1),
                        solve(value + toppingCosts[j], j + 1),
                        solve(value, j + 1),
                        key = lambda x: (abs(target - x), x)
                    )

        return min([solve(base) for base in baseCosts], key = lambda x: (abs(target - x), x))

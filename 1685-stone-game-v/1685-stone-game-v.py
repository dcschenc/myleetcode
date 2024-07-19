class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1563.Stone%20Game%20V
        @cache
        def dp(left, right):
            if left >= right:
                return 0
            ans, a = 0, 0
            for i in range(left, right):
                a += stoneValue[i]
                b = prefix_sums[right + 1] - prefix_sums[left] - a
                if a < b:
                    if ans > 2*a:
                        break
                    ans = max(ans, a + dp(left, i))
                elif a > b:
                    if ans > 2*b:
                        break
                    ans = max(ans, b + dp(i + 1, right))
                else:
                    ans = max(ans, a + dp(left, i), b + dp(i + 1, right))
            
            return ans
        
        prefix_sums = list(accumulate(stoneValue, initial=0))
        return dp(0, len(stoneValue) - 1)
            
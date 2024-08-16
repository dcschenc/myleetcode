class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3000-3099/3085.Minimum%20Deletions%20to%20Make%20String%20K-Special
        def f(v: int) -> int:
            ans = 0
            for x in nums:
                if x < v:
                    ans += x
                elif x > v + k:
                    ans += x - v - k
            return ans

        nums = Counter(word).values()
        mx = max(nums)
        return min(f(v) for v in range(mx + 1))
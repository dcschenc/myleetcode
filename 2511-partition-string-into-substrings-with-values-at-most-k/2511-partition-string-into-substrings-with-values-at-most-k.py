class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2522.Partition%20String%20Into%20Substrings%20With%20Values%20at%20Most%20K
        @cache
        def backtrack(i):
            if i == n:
                return 0
            ans, v = float('inf'), 0
            for j in range(i, n):
                v = v * 10 + int(s[j])
                if v > k:
                    break
                ans = min(ans, 1 + backtrack(j + 1))
            return ans
            
        n = len(s)
        ans = backtrack(0)
        return ans if ans != float('inf') else -1
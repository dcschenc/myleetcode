class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3100-3199/3186.Maximum%20Total%20Damage%20With%20Spell%20Casting
        @cache
        def dfs(i: int) -> int:
            if i >= n:
                return 0
            a = dfs(i + cnt[power[i]])
            b = power[i] * cnt[power[i]] + dfs(nxt[i])
            return max(a, b)

        n = len(power)
        cnt = Counter(power)
        power.sort()
        nxt = [bisect_right(power, x + 2, lo=i + 1) for i, x in enumerate(power)]
        return dfs(0)
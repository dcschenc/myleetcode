class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2305.Fair%20Distribution%20of%20Cookies
        def backtrack(idx):
            nonlocal ans
            if idx > len(cookies):
                return
            if idx == len(cookies):
                ans = min(ans, max(combo))
                return
            for i in range(k):
                if combo[i] + cookies[idx] >= ans:  ### pruning
                    continue
                combo[i] += cookies[idx]
                backtrack(idx + 1)
                combo[i] -= cookies[idx]       

        ans = inf
        cookies.sort(reverse=True)  ## this is important
        combo = [0] * k
        backtrack(0)
        return ans

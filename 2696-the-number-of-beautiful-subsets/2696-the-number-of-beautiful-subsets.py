class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def backtrack(i, path):
            if len(path) != 0:
                ans[0] += 1
            for j in range(i, n):
                if len(path) == 0 or nums[j] - k not in path:
                    backtrack(j + 1, path + [nums[j]])
        nums.sort()
        ans, n = [0], len(nums)
        backtrack(0, [])
        return ans[0]

        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            # ans += 1
            seen = set()
            seen.add(nums[i])
            for j in range(i+1, n):
                if nums[j] - k in seen:
                    continue
                seen.add(nums[j])
            cnt = len(seen)
            ans += (cnt + 1) * cnt//2
                # ans += 1
        return ans
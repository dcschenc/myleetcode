class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2910.Minimum%20Number%20of%20Groups%20to%20Create%20a%20Valid%20Assignment
        cnt = Counter(nums)
        mi = min(cnt.values())
        for k in range(mi, 0, -1):
            ans = 0
            for v in cnt.values():
                if v // k < v % k:
                    ans = 0
                    break
                ans += (v + k) // (k + 1)

            if ans != 0:
                return ans
        
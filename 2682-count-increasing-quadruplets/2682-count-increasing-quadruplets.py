class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/count-increasing-quadruplets/solutions/3111697/c-java-python3-cleanest-code-with-clarification-o-n-2/
        n = len(nums)
        cnt = [0] * n
        ans = 0
        for j in range(n):
            prev_small = 0
            for i in range(j):
                if nums[j] > nums[i]:
                    prev_small += 1
                    ans += cnt[i]
                elif nums[j] < nums[i]:
                    cnt[i] += prev_small
        return ans
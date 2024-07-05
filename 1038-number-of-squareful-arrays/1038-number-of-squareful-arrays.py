class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def backtrack(path):
            if len(path) == n:
                ans[0] += 1
                return
            for i in range(n):
                if i > 0 and nums[i] == nums[i-1] and visited[i-1] == False:
                    continue
                if visited[i] is False:
                    if len(path) == 0 or len(path) > 0 and sqrt(path[-1] + nums[i]).is_integer():
                        visited[i] = True
                        backtrack(path + [nums[i]])
                        visited[i] = False

        n, ans = len(nums), [0]
        visited = [False] * n
        nums.sort()
        backtrack([])
        return ans[0]

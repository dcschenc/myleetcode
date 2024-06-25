class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def dfs(num):
            if num in cur_visited:
                return
            cur_visited.add(num)
            dfs(nums[num])

        visited = set()
        cur_visited = set()
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] not in visited:                
                cur_visited = set()
                dfs(nums[i])
                ans = max(ans, len(cur_visited))
                visited.update(cur_visited)
        # print(visited)
        return ans
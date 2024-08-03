class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        for i, j in queries:
            cur = []
            for k, num in enumerate(nums):
                cur.append((int(num[-j:]), k))
            cur.sort()
            ans.append(cur[i-1][1])
        return ans
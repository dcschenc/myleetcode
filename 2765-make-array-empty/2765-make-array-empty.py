from sortedcontainers import SortedList
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2659.Make%20Array%20Empty
        pos = {x: i for i, x in enumerate(nums)}
        nums.sort()
        sl = SortedList()
        ans = pos[nums[0]] + 1
        n = len(nums)
        for k, (a, b) in enumerate(pairwise(nums)):
            i, j = pos[a], pos[b]
            d = j - i - (sl.bisect(j) - sl.bisect(i))
            ans += d + (n - k) * int(i > j)
            sl.add(i)
        return ans

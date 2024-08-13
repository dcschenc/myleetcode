from collections import deque
class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = deque()
        k = 0
        ans = []
        for i, num in enumerate(nums):
            if num > 0:
                seen.appendleft(num)
                k = 0
            else:
                if k >= len(seen):
                    ans.append(-1)
                else:
                    ans.append(seen[k])
                k += 1
        return ans

from sortedcontainers import SortedList
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1753.Maximum%20Score%20From%20Removing%20Stones
        s = sorted([a, b, c])
        ans = 0
        while s[1]:
            ans += 1
            s[1] -= 1
            s[2] -= 1
            s.sort()
        return ans
        
        # scores = 0
        # arr = SortedList([a, b, c])
        # while len(arr) >= 2:
        #     x = arr[0]
        #     y = arr[-1]
        #     arr.remove(x)
        #     if x - 1 > 0:
        #         arr.add(x-1)
        #     arr.remove(y)
        #     if y - 1 > 0:
        #         arr.add(y-1)
        #     scores += 1
        # return scores
        
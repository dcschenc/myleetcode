class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1200-1299/1291.Sequential%20Digits
        ans = []
        for i in range(1, 9):
            x = i
            for j in range(i + 1, 10):
                x = x * 10 + j
                if low <= x <= high:
                    ans.append(x)
        return sorted(ans)

        # ans = []
        # for i in range(1, 10):
        #     cur = i
        #     while cur <= high:
        #         if cur >= low:
        #             ans.append(cur)
        #         nxt = int(str(cur)[-1])
        #         if  nxt + 1 <= 9:
        #             cur = cur * 10 + nxt + 1
        #         else:
        #             break
        # ans.sort()
        # return ans
        
                

        
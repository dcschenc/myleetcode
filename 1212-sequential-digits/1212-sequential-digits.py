class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for i in range(1, 10):
            cur = i
            while cur <= high:
                if cur >= low:
                    ans.append(cur)
                nxt = int(str(cur)[-1])
                if  nxt + 1 <= 9:
                    cur = cur * 10 + nxt + 1
                else:
                    break
        ans.sort()
        return ans
        
                

        
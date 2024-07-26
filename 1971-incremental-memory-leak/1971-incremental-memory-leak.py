class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1860.Incremental%20Memory%20Leak
        i = 1
        while i <= max(memory1, memory2):
            if memory1 >= memory2:
                memory1 -= i
            else:
                memory2 -= i
            i += 1
        return [i, memory1, memory2]
        
        heaps = []
        heappush(heaps, (-memory1, 1))
        heappush(heaps, (-memory2, 2))
        i = 1
        while True:
            # print(i, heaps)
            mx, stick = heaps[0]
            mx = -mx
            if mx < i:
                ans = [i, 0, 0]
                ans[heaps[0][1]] = -heaps[0][0]
                ans[heaps[1][1]] = -heaps[1][0]
                return ans            
            heappop(heaps)
            heappush(heaps, (-(mx - i), stick))
            i += 1

                
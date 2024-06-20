class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seen = {1, }
        ans = 1
        heap = []
        heappush(heap, 1)
        for _ in range(n):
            ans = heappop(heap)
            # nums.append(cur_ugly)
            for i in [2, 3, 5]:
                nxt = ans * i
                if nxt not in seen:
                    seen.add(nxt)
                    heappush(heap, nxt)
        return ans

        ugly_numbers = [1]  
        p2, p3, p5 = 0, 0, 0 

        while len(ugly_numbers) < n:            
            next_ugly = min(ugly_numbers[p2] * 2, ugly_numbers[p3] * 3, ugly_numbers[p5] * 5)

            # Move the pointers for the multiples whose product gave the next ugly number
            if next_ugly == ugly_numbers[p2] * 2:
                p2 += 1
            if next_ugly == ugly_numbers[p3] * 3:
                p3 += 1
            if next_ugly == ugly_numbers[p5] * 5:
                p5 += 1

            ugly_numbers.append(next_ugly)

        return ugly_numbers[-1]
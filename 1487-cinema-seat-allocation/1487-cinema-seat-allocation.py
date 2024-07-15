class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1386.Cinema%20Seat%20Allocation
        d = defaultdict(int)
        for i, j in reservedSeats:
            d[i] |= 1 << (10 - j)
        masks = (0b0111100000, 0b0000011110, 0b0001111000)
        ans = (n - len(d)) * 2
        for x in d.values():
            for mask in masks:
                if (x & mask) == 0:
                    x |= mask
                    ans += 1
        return ans

        hm = defaultdict(set)        
        for r, c in reservedSeats:
            hm[r].add(c)
        ans = (n - len(hm.keys())) * 2
        left, mid, right = {2, 3, 4, 5}, {4, 5, 6, 7}, {6, 7, 8, 9}
        # for i in range(1, n + 1):  ## when n is very large, memory issue
        for i in hm.keys():    
            if not left & hm[i]:
                ans += 1
                if not right & hm[i]:
                    ans += 1
            elif not mid & hm[i]:
                ans += 1
            elif not right & hm[i]:
                ans += 1
            i += 1
        return ans

        
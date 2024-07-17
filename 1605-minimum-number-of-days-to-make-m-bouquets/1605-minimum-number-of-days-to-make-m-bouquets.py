class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:    
        def can_make(days):
            cur = cnt = 0
            for num in bloomDay:
                if days >= num:
                    cur += 1
                    if cur == k:
                        cnt += 1
                        cur = 0
                else:
                    cur = 0
            return cnt >= m
            
        if m * k > len(bloomDay):
            return -1

        max_days = max(bloomDay)
        left, right = 0, max_days
        while left < right:
            mid = (left + right)//2
            res = can_make(mid)
            if res is True:
                right = mid
            else:
                left = mid + 1
        # print(left, right)
        return left
        # return right if can_make(right) else -1
        

        # if m*k > len(bloomDay):
        #     return -1
        # bloomDay.sort()
        # return bloomDay[m*k-1]
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1701.Average%20Waiting%20Time
        cur = 0
        n, total = len(customers), 0
        for i, (s, e) in enumerate(customers):
            if cur < s:
                total += e
                cur = s
            else:
                total += cur - s + e
            cur = cur + e
            # print(i, cur, total)
        return total/n

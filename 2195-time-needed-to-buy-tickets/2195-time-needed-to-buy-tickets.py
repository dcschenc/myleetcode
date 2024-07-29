class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2073.Time%20Needed%20to%20Buy%20Tickets
        ans = 0
        for i, x in enumerate(tickets):
            ans += min(x, tickets[k] if i <= k else tickets[k] - 1)
        return ans
        
        n, time = len(tickets), 0
        while True:
            for i in range(n):
                if tickets[i] > 0:
                    time += 1
                    tickets[i] -= 1
                if k == i and tickets[k] == 0:
                    return time

        
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2483.Minimum%20Penalty%20for%20a%20Shop
        ans, hour = float('inf'), float('inf')
        cnt_y = customers.count('Y')
        cur_y, cur_n = 0, 0
        n = len(customers)
        for i in range(n + 1):
            penalty = cnt_y - cur_y + cur_n
            if penalty < ans:
                ans = penalty
                hour = i            
            if i == n: 
                break
            if customers[i] == 'Y':
                cur_y += 1
            else:
                cur_n += 1
        return hour
            
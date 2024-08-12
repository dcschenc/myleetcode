class Solution:
    def smallestNumber(self, n: int) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2847.Smallest%20Number%20With%20Given%20Digit%20Product
        cnt = [0] * 10
        for i in range(9, 1, -1):
            while n % i == 0:
                n //= i
                cnt[i] += 1
        if n > 1:
            return "-1"
        ans = "".join(str(i) * cnt[i] for i in range(2, 10))
        return ans if ans else "1"
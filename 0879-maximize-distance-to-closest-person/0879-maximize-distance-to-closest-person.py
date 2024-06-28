class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0800-0899/0849.Maximize%20Distance%20to%20Closest%20Person
        first = last = None
        d = 0
        for i, c in enumerate(seats):
            if c:
                if last is not None:
                    d = max(d, i - last)
                if first is None:
                    first = i
                last = i
        return max(first, len(seats) - last - 1, d // 2)


        n = len(seats)
        prefix, postfix = [0] * n, [0] * n
        prev = -1
        for i in range(n):
            if seats[i] == 1:
                prefix[i] = 0
                prev = i
            elif prev == -1:
                prefix[i] = 0
            else:
                prefix[i] = i - prev
        prev = -1
        for i in range(n-1, -1, -1):
            if seats[i] == 1:
                postfix[i] = 0
                prev = i
            elif prev == -1:
                postfix[i] = 0
            else:
                postfix[i] = prev - i
        # print(prefix, postfix)
        ans = 0
        for i in range(n):
            if seats[i] == 0:
                if postfix[i] == 0 or prefix[i] == 0:
                    ans = max(ans, max(prefix[i], postfix[i]))
                else:
                    ans = max(ans, min(prefix[i], postfix[i]))
        return ans
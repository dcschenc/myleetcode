class Solution:
    def countTime(self, time: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2437.Number%20of%20Valid%20Clock%20Times
        def check(s: str, t: str) -> bool:
            return all(a == b or b == '?' for a, b in zip(s, t))

        return sum(
            check(f'{h:02d}:{m:02d}', time) for h in range(24) for m in range(60)
        )

        # h1 = h2 = 1
        # if time[0] == '?':
        #     if time[1] == '?':
        #         h1 = 2 * 10 + 1 * 4
        #     elif time[1] <= '3' or time[1] == '4' and time[3] == '0' and time[4] == '0':
        #         h1 = 3           
        #     else:
        #         h1 = 2
        # else:
        #     if time[1] == '?':
        #         if time[0] in ['0', '1']:
        #             h1 = 10
        #         else:
        #             h1 = 4
        # if time[3] == '?':
        #     h2 = 6
        # if time[4] == '?':
        #     h2 *= 10
        # return h1 * h2

        # for i, c in enumerate(time):
        #     if c == '?':
        #         match i:
        #             case 0:
        #                 if '0' <= time[1] <= '4':
        #                     h1 = 3
        #                 else:
        #                     h1 = 2
        #             case 1:
        #                 h2 = 10
        #             case 3:
        #                 h3 = 10
        #             case 4:
        #                 h4 = 10
        # return h1 * h2 * h3 * h4
                
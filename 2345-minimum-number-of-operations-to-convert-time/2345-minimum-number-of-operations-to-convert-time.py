class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        a = int(current[:2]) * 60 + int(current[3:])
        b = int(correct[:2]) * 60 + int(correct[3:])
        ans, d = 0, b - a
        for i in [60, 15, 5, 1]:
            ans += d // i
            d %= i
        return ans

        # hour1, hour2 = int(current[:2]), int(correct[:2])
        # min1, min2 = int(current[3:]), int(correct[3:])
        # diff = (hour2 - hour1) * 60 + (min2 - min1)
        # ans = 0
        # for d in [60, 15, 5, 1]:
        #     while diff >= d:
        #         ans += 1
        #         diff -= d
        # return ans
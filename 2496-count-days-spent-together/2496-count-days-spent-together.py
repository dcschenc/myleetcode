class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        start = sum(months[:int(start[:2])-1]) + int(start[3:])
        end = sum(months[:int(end[:2])-1]) + int(end[3:])
        days = max(end - start + 1, 0)
        return days
        
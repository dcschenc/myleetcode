from collections import deque
class Solution:
    # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1989.Maximum%20Number%20of%20People%20That%20Can%20Be%20Caught%20in%20Tag
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        ans = j = 0
        n = len(team)
        for i, x in enumerate(team):
            if x:
                while j < n and (team[j] or i - j > dist):
                    j += 1
                if j < n and abs(i - j) <= dist:
                    ans += 1
                    j += 1
        return ans

        cnt = 0
        n = len(team)
        zeros = deque()
        ones = deque()
        for i in range(n):
            if team[i] == 0:
                if len(ones) > 0:
                    cnt += 1
                    ones.popleft()
                else:
                    zeros.append(i)
            else:
                if len(zeros) > 0:
                    cnt += 1
                    zeros.popleft() 
                else:
                    ones.append(i)

            if ones and i - ones[0] >= dist:
                ones.popleft()
            if zeros and i - zeros[0] >= dist:
                zeros.popleft()
        return cnt

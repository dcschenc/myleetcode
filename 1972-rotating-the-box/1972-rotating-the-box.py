class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1861.Rotating%20the%20Box
        # m, n = len(box), len(box[0])
        # ans = [[None] * m for _ in range(n)]
        # for i in range(m):
        #     for j in range(n):
        #         ans[j][m - i - 1] = box[i][j]
        # for j in range(m):
        #     q = deque()
        #     for i in range(n - 1, -1, -1):
        #         if ans[i][j] == '*':
        #             q.clear()
        #         elif ans[i][j] == '.':
        #             q.append(i)
        #         elif q:
        #             ans[q.popleft()][j] = '#'
        #             ans[i][j] = '.'
        #             q.append(i)
        # return ans

        m, n = len(box), len(box[0])
        ans = [['.' for j in range(m)] for i in range(n)]
        for i in range(m):
            s = ''.join(box[i])
            row = ''
            for sub in s.split('*'):
                cnt = sub.count('#')
                row += '.' * (len(sub) - cnt) + '#' * cnt + '*'
            box[i] = list(row)
        for i in range(m):
            for j in range(n):
                ans[j][m-i-1] = box[i][j]
        return ans

        
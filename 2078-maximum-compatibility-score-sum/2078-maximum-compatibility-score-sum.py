class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1947.Maximum%20Compatibility%20Score%20Sum
        def backtrack(idx, cur):
            if idx == n:
                ans[0] = max(ans[0], cur)
                return
            for j in range(n):
                if assigned[j] is False:
                    score = scores[(idx, j)]
                    assigned[j] = True
                    backtrack(idx + 1, cur + score)
                    assigned[j] = False

        ans, n, m = [0], len(students), len(students[0])     
        scores = defaultdict(int)        
        for i in range(n):
            for j in range(n):
                for k in range(m):
                    if students[i][k] == mentors[j][k]:
                        scores[(i,j)] += 1 
        assigned = [False] * n
        for j in range(n):
            assigned[j] = True
            backtrack(1, scores[(0, j)])
            assigned[j] = False
        return ans[0]


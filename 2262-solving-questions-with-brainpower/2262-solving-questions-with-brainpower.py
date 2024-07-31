class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2140.Solving%20Questions%20With%20Brainpower
        @cache
        def dfs(i):
            if i >= n:
                return 0
            if i == n - 1:
                return questions[i][0]
            score, skip = questions[i]
            ans = max(score + dfs(i + skip + 1), dfs(i + 1))
            return ans
        n = len(questions)
        # print(n)
        return dfs(0)        
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2375.Construct%20Smallest%20Number%20From%20DI%20String
        # def dfs(u):
        #     nonlocal ans
        #     if ans:
        #         return
        #     if u == len(pattern) + 1:
        #         ans = ''.join(t)
        #         return
        #     for i in range(1, 10):
        #         if not vis[i]:
        #             if u and pattern[u - 1] == 'I' and int(t[-1]) >= i:
        #                 continue
        #             if u and pattern[u - 1] == 'D' and int(t[-1]) <= i:
        #                 continue
        #             vis[i] = True
        #             t.append(str(i))
        #             dfs(u + 1)
        #             vis[i] = False
        #             t.pop()

        # vis = [False] * 10
        # t = []
        # ans = None
        # dfs(0)
        # return ans
        
        # pattern += 'I'
        # res = s = ''
        # for i, p in enumerate(pattern):
        #     s += str(i+1)
        #     if p == 'I':
        #         res += s[::-1]
        #         s =''
        # return res

        ans = []
        stack = []
        for i in range(len(pattern)+1): 
            stack.append(str(i+1))
            if i == len(pattern) or pattern[i] == 'I': 
                while stack: 
                    ans.append(stack.pop())
        return ''.join(ans) 

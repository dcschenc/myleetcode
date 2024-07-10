class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1200-1299/1215.Stepping%20Numbers

        #### BFS ####
        ans = []
        if low == 0:
            ans.append(0)
        q = deque(range(1, 10))
        while q:
            v = q.popleft()
            if v > high:
                break
            if v >= low:
                ans.append(v)
            x = v % 10
            if x >= 1:
                q.append(v * 10 + x - 1)
            if x < 9:
                q.append(v * 10 + x + 1)
        return ans

        #### backtrack ####
        def get_num(path):
            ans = 0
            for i, d in enumerate(path):
                ans = ans * 10  +  d
            return ans

        def backtrack(idx, path):
            num = get_num(path)
            if num > high:
                return False
            if num >= low:
                ans.append(num)
            for i in range(0, 10):
                if idx == 1 and i == 0: 
                    continue
                if idx == 1 or idx > 1 and abs(i - path[-1]) == 1:
                    res = backtrack(idx + 1, path + [i])
                    if res is False:
                        break
            
        ans = []
        backtrack(1, [])
        ans.sort()
        return ans        
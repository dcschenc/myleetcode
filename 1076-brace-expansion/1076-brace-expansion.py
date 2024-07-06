class Solution:
    def expand(self, s: str) -> List[str]:
        def backtrack(idx, path):
            if idx == n:
                res.append(path)
                return
            candidates = []
            if s[idx] == '{':
                j = idx + 1
                while j < n and s[j] != '}':
                    if s[j] != ',':
                        candidates.append(s[j])
                    j += 1
                idx = j
            else:
                candidates =[s[idx]]
            for c in candidates:
                backtrack(idx + 1, path + c)

        res = []
        n = len(s)
        backtrack(0, '')
        res.sort()
        return res

        def convert(s):
            if not s:
                return
            if s[0] == '{':
                j = s.find('}')
                items.append(s[1:j].split(','))
                convert(s[j + 1 :])
            else:
                j = s.find('{')
                if j != -1:
                    items.append(s[:j].split(','))
                    convert(s[j:])
                else:
                    items.append(s.split(','))

        def dfs(i, t):
            if i == len(items):
                ans.append(''.join(t))
                return
            for c in items[i]:
                t.append(c)
                dfs(i + 1, t)
                t.pop()

        items = []
        convert(s)
        ans = []
        dfs(0, [])
        ans.sort()
        return ans
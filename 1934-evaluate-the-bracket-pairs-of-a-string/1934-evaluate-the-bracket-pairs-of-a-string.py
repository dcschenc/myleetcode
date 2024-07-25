class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1807.Evaluate%20the%20Bracket%20Pairs%20of%20a%20String
        d = {a: b for a, b in knowledge}
        i, n = 0, len(s)
        ans = []
        while i < n:
            if s[i] == '(':
                j = s.find(')', i + 1)
                ans.append(d.get(s[i + 1 : j], '?'))
                i = j
            else:
                ans.append(s[i])
            i += 1
        return ''.join(ans)


        hm = {}
        for a, b in knowledge:
            hm[a] = b
        i, n = 0, len(s)
        ans = ''
        while i < n:
            if s[i] != '(':
                ans += s[i]
                i += 1
            else:
                j = i
                while j + 1 < n and s[j + 1] != ')':
                    j += 1
                k = s[i+1:j+1]
                if k in hm:
                    ans += hm[k]
                else:
                    ans += '?'
                i = j + 2
        return ans
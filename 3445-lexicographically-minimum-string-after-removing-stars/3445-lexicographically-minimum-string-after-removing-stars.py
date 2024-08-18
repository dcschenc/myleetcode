class Solution:
    def clearStars(self, s: str) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/3100-3199/3170.Lexicographically%20Minimum%20String%20After%20Removing%20Stars
        g = defaultdict(list)
        n = len(s)
        rem = [False] * n
        for i, c in enumerate(s):
            if c == "*":
                rem[i] = True
                for a in ascii_lowercase:
                    if g[a]:
                        rem[g[a].pop()] = True
                        break
            else:
                g[c].append(i)
        return "".join(c for i, c in enumerate(s) if not rem[i])
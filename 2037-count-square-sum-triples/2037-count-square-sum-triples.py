class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                c = math.sqrt(i*i + j*j)                
                if c <= n and int(c) == c:
                    ans += 1
                    # print(i, j, c)
        return ans

        ans = 0
        sq = []
        for i in range(1, n+1):
            sq.append(i*i)
        # sq.sort()
        seen = set(sq)
        for i in range(len(sq)):
            for j in range(len(sq)):                
                    if sq[i] + sq[j] in seen:
                        ans += 1
        return ans

        # for i in range(1, n + 1):
        #     for j in range(1, n + 1):
        #         for k in range(1, n + 1):
        #             if i*i + j*j == k*k:
        #                 ans += 1
        # return ans
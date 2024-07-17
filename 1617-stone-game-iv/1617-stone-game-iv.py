class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # @cache
        # def dfs(i: int) -> bool:
        #     if i == 0:
        #         return False
        #     j = 1
        #     while j * j <= i:
        #         if not dfs(i - j * j):
        #             return True
        #         j += 1
        #     return False

        # return dfs(n)


        @cache
        def df(i):
            if i == 0:
                return False
            if math.sqrt(i) == int(math.sqrt(i)):
                return True
            ans = False
            for j in range(1, int(math.sqrt(i)) + 1):
                if not df(i - j * j):
                    ans = True
            return ans

        return df(n)
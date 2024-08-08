class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2611.Mice%20and%20Cheese
        n = len(reward1)
        idx = sorted(range(n), key=lambda i: reward1[i] - reward2[i], reverse=True)
        return sum(reward1[i] for i in idx[:k]) + sum(reward2[i] for i in idx[k:])
                
        pairs = list(zip(reward1, reward2))
        pairs.sort(key=lambda x: (x[0] -x[1]), reverse=True)
        ans = 0
        for i in range(k):
            ans += pairs[i][0]
        n = len(pairs)
        for i in range(k, n):
            ans += pairs[i][1]
        return ans
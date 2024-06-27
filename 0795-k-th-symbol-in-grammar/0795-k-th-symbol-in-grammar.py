class Solution:
    hm = {}
    def kthGrammar(self, n: int, k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0700-0799/0779.K-th%20Symbol%20in%20Grammar
        if n == 1: 
            return 0
        mid = math.pow(2, n - 1) // 2
        if k <= mid:
            return self.kthGrammar(n - 1, k) # The Kth bit will be same as parent level when k<=mid
        else:
            return 1 - self.kthGrammar(n - 1, k - mid) #The Kth bit will be opposite as parent level when k<=mid
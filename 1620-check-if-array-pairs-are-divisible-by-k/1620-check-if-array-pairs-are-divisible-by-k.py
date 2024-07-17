class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1497.Check%20If%20Array%20Pairs%20Are%20Divisible%20by%20k
        cnt = Counter(x % k for x in arr)
        return cnt[0] % 2 == 0 and all(cnt[i] == cnt[k - i] for i in range(1, k))
        
        n = len(arr)
        mod = []
        zeros = 0
        for i in range(n):
            if arr[i] % k == 0:
                zeros += 1
            else:
                mod.append(arr[i] % k)
        if zeros % 2 == 1: return False  
             
        mod.sort()
        m = len(mod)
        for i in range(m//2):
            if mod[i] + mod[m - 1 - i] != k:
                return False
        return True
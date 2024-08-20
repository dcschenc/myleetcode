class Solution:
    def minChanges(self, n: int, k: int) -> int:
        n, k = list(f'{n:032b}'), list(f'{k:032b}')
        # print(n, k)
        total = 0
        for i, (a, b) in enumerate(zip(n, k)):
            if a != b:
                if a == '1':
                    n[i] = '0'
                    total += 1
                else:
                    return -1
        return total

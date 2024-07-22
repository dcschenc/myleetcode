class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans
        for i in range(n):
            if k > 0:
                for j in range(i + 1, i + k + 1):
                    ans[i] += code[j % n]
            else:
                for j in range(i + k, i):
                    ans[i] += code[(j + n) % n]
        return ans

        
        ans = []
        n = len(code)
        for i in range(n):
            if k == 0:
                ans.append(0)
            elif k > 0:
                cur = 0
                for j in range(1, k+1):
                    cur += code[(i + j) % n]
                ans.append(cur)
            else:
                cur = 0
                for j in range(1, abs(k)+1):
                    cur += code[(i-j) % n]
                ans.append(cur)
        return ans
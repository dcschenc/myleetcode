class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for n in range(left, right + 1):
            if '0' in str(n): continue
            if all(n % int(d) == 0 for d in str(n)):
                ans.append(n)
        return ans
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        if len(original) != m * n:
            return []
        i = 0
        while i < m:
            ans.append(original[i * n : i * n + n ])
            i += 1
        return ans
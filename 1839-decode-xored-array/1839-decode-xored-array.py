class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        n = len(encoded)
        for i in range(n):
            cur = encoded[i] ^ ans[-1]
            ans.append(cur)
        return ans
        
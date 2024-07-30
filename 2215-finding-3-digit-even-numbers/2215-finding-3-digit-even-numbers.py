class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        n = len(digits)
        for a, b, c in permutations(digits, 3):
            cur = 100 * a + 10  * b + c
            if cur % 2 == 0 and cur >= 100:
                ans.add(cur)
        # for i in range(n):           
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         for k in range(n):
        #             if k == j or k == i:
        #                 continue
        #             cur = digits[i] * 100 + digits[j] * 10 + digits[k]
        #             if cur % 2 == 0 and cur >= 100:
        #                 ans.add(cur)
        return sorted(list(ans))
        
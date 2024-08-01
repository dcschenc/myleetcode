class Solution:
    def singleDivisorTriplet(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2198.Number%20of%20Single%20Divisor%20Triplets
        cnt = Counter(nums)
        ans = 0
        for a, x in cnt.items():
            for b, y in cnt.items():
                for c, z in cnt.items():
                    s = a + b + c
                    if sum(s % v == 0 for v in (a, b, c)) == 1:
                        if a == b:
                            ans += x * (x - 1) * z
                        elif a == c:
                            ans += x * (x - 1) * y
                        elif b == c:
                            ans += x * y * (y - 1)
                        else:
                            ans += x * y * z
        return ans
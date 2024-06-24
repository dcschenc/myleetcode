class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # I feel companies are asking this question to test on Dr Claude Shannon's Information Theory. Each pig can carry log(minutesToTest / minutesToDie + 1) bit of information. To identify the bucket, we need log(buckets) bit of information. Which means, we need Ceil(log(buckets)/log(minutesToTest / minutesToDie + 1)) pigs.

        base = minutesToTest // minutesToDie + 1
        res, p = 0, 1
        while p < buckets:
            p *= base
            res += 1
        return res
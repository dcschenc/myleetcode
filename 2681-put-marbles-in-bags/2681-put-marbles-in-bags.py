class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2551.Put%20Marbles%20in%20Bags
        arr = sorted(a + b for a, b in pairwise(weights))
        return sum(arr[len(arr) - k + 1 :]) - sum(arr[: k - 1])

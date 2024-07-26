class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        batch = sum(chalk)
        if k % batch == 0:
            return 0
        k = k % batch
        for i, num in enumerate(chalk):
            if k < num:
                return i
            k -= num
        
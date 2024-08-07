class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2554.Maximum%20Number%20of%20Integers%20to%20Choose%20From%20a%20Range%20I
        banned, total, cnt = set(banned), 0, 0
        for i in range(1, n + 1):            
            if i not in banned:
                if total + i > maxSum:
                    break
                cnt += 1
                total += i
                # banned.add(i)
        return cnt
                
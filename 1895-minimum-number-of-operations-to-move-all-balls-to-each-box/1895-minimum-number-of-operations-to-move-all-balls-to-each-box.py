class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1769.Minimum%20Number%20of%20Operations%20to%20Move%20All%20Balls%20to%20Each%20Box
        n = len(boxes)
        left = [0] * n
        right = [0] * n
        cnt = 0
        for i in range(1, n):
            if boxes[i - 1] == '1':
                cnt += 1
            left[i] = left[i - 1] + cnt
        cnt = 0
        for i in range(n - 2, -1, -1):
            if boxes[i + 1] == '1':
                cnt += 1
            right[i] = right[i + 1] + cnt
        return [a + b for a, b in zip(left, right)]

        # ans = [0] * len(boxes)
        # idx_1 = []
        # for i in range(len(boxes)):
        #     if boxes[i] == '1':
        #         idx_1.append(i)
        # for i in range(len(boxes)):
        #     for j in idx_1:
        #         if i != j:
        #             ans[i] += abs(j - i)
        # return ans

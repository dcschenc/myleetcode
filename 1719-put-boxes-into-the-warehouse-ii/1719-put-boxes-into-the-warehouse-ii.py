class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1580.Put%20Boxes%20Into%20the%20Warehouse%20II
        boxes.sort()
        n = len(warehouse)
        min_left, cur = [0] * n, float('inf')
        min_idx = 0
        for i, h in enumerate(warehouse):
            if h < cur:
                cur = h
                min_idx = i
            min_left[i] = cur

        min_right, cur = [0] * n, float('inf')
        for i in range(n-1, -1, -1):
            if warehouse[i] < cur:
                cur = warehouse[i]
            min_right[i] = cur

        left, right, ans = min_idx, min_idx + 1, 0
        for b in boxes:
            while left >= 0 and min_left[left] < b:
                left -= 1
            while right < n and min_right[right] < b:
                right += 1
            
            if left >= 0 and right <= n - 1:
                if min_left[left] < min_right[right]:
                    left -= 1
                else:
                    right += 1
                ans += 1
            elif left >= 0:
                ans += 1
                left -= 1
            elif right <= n -1:
                ans += 1
                right += 1
            else:
                break
        return ans
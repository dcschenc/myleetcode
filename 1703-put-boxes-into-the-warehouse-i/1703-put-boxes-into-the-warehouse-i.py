class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # https://github.com/doocs/leetcode/blob/main/solution/1500-1599/1564.Put%20Boxes%20Into%20the%20Warehouse%20I/README.md
        boxes.sort()
        n = len(warehouse)
        min_h = [0] * n
        cur = float('inf')
        for i, h in enumerate(warehouse):
            if h < cur:
                cur = h
            min_h[i] = cur

        w, ans = n - 1, 0
        for b in boxes:
            while w >= 0 and min_h[w] < b:
                w -= 1
            if w >= 0:
                ans += 1
                w -= 1
            else:
                break
        return ans 


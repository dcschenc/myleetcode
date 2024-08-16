class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        ans = 0
        for i in range(len(capacity)):
            ans += 1
            total -= capacity[i]
            if total <= 0:
                return ans
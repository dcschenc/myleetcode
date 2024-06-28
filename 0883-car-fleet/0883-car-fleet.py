class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0800-0899/0853.Car%20Fleet
        idx = sorted(range(len(position)), key=lambda i: position[i])
        ans = pre = 0
        for i in idx[::-1]:
            t = (target - position[i]) / speed[i]
            if t > pre:
                ans += 1
                pre = t
        return ans
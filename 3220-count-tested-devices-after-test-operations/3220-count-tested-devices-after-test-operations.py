class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        b = batteryPercentages
        n = len(b)
        ans = 0
        for i in range(n):
            if b[i] > 0:
                ans += 1
                for j in range(i+1, n):
                    b[j] -= 1
        return ans
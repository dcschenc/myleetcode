class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2126.Destroying%20Asteroids
        asteroids.sort()
        for num in asteroids:
            if mass >= num:
                mass += num
            else:
                return False
        return True
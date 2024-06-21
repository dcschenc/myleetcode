class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:

        seen = set()

        def dfs(tot):
            if tot == targetCapacity:
                return True
            if tot in seen or tot < 0 or tot > jug1Capacity + jug2Capacity:
                return False
            
            seen.add(tot)

            return dfs(tot+jug1Capacity) or dfs(tot-jug1Capacity) or dfs(tot+jug2Capacity) or dfs(tot-jug2Capacity)
        
        return dfs(0)

        # Check if the total amount to be measured exceeds the sum of jug capacities
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False

        # Check if the target amount can be formed using the greatest common divisor (GCD)
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        return targetCapacity == 0 or targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0
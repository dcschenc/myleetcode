class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2079.Watering%20Plants
        n, i = len(plants), 0
        steps = 0
        while i < n:            
            used = plants[i]
            j = i + 1
            while j < n and used + plants[j] <= capacity:                
                used += plants[j]
                j += 1
            steps += j
            i = j
            if i < n:
                steps += j

        return steps

            
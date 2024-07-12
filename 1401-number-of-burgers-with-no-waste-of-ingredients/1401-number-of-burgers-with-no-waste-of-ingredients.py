class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1200-1299/1276.Number%20of%20Burgers%20with%20No%20Waste%20of%20Ingredients
        
        # Check for the basic constraints
        if tomatoSlices < 0 or cheeseSlices < 0 or tomatoSlices % 2 != 0 or tomatoSlices < 2 * cheeseSlices or tomatoSlices > 4 * cheeseSlices:
            return []

        # Calculate x and y
        x = (tomatoSlices - 2 * cheeseSlices) // 2
        y = cheeseSlices - x

        # Check if x and y are non-negative
        if x < 0 or y < 0:
            return []

        return [x, y]
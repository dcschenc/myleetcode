class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1798.Maximum%20Number%20of%20Consecutive%20Values%20You%20Can%20Make
        # Sort the coins
        coins.sort()
        
        # Initialize the maximum number of consecutive values we can form
        max_consecutive = 0
        
        # Iterate through the sorted coins
        for coin in coins:
            # If the coin's value is greater than max_consecutive + 1, we cannot form max_consecutive + 1
            if coin > max_consecutive + 1:
                break
            # Otherwise, add the coin's value to max_consecutive
            max_consecutive += coin
        
        return max_consecutive + 1
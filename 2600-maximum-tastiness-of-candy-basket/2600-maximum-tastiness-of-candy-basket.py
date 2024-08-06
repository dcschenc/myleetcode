class Solution:
    def maximumTastiness(self, prices: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2517.Maximum%20Tastiness%20of%20Candy%20Basket
        # https://algo.monster/liteproblems/2517
        def is_possible(minimum_distance: int) -> bool:
            # Initialize counter for number of cakes and the previous cake's price
            count, previous_price = 0, -minimum_distance
          
            # Iterate through sorted prices
            for current_price in prices:
                # If the distance from the previous selected cake price is
                # at least the minimum distance, select this cake
                if current_price - previous_price >= minimum_distance:
                    previous_price = current_price
                    count += 1
          
            # Check if we can select at least `target_count` number of cakes
            return count >= k

        # Sort the price list to enable binary search
        prices.sort()

        # Initialize binary search boundaries for the minimum distance
        left, right = 0, prices[-1] - prices[0]
      
        # Perform binary search to find the maximum minimum distance
        while left < right:
            # Compute the middle value between left and right
            middle = (left + right + 1) // 2          
            # If it's possible to choose `target_count` cakes with at least 
            # `middle` distance between them, move to the right half
            if is_possible(middle):
                left = middle
            else:
                # Otherwise, continue with the left half
                right = middle - 1      
        # The maximum minimum distance will be `left` after binary search ends
        return left

        
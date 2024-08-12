class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        # https://algo.monster/liteproblems/2813        
        # Sort the items by price in descending order
        items.sort(key=lambda x: -x[0])
        total_price = 0
        seen_colors = set()
        duplicate_prices = []

        # Process the first K items and calculate their total price
        # Record if a color has been seen before and keep track of duplicates
        for price, color in items[:k]:
            total_price += price
            if color not in seen_colors:
                seen_colors.add(color)
            else:
                duplicate_prices.append(price)

        # Calculate the current elegance as the sum of prices and the square of
        # unique colors count
        max_elegance = total_price + len(seen_colors) ** 2

        # Process the rest of the items beyond the initial K
        for price, color in items[k:]:
            # If the color is already seen or there are no duplicates, continue
            if color in seen_colors or not duplicate_prices:
                continue

            # Add the new color to the seen set
            seen_colors.add(color)
          
            # Update the total price by swapping the lowest duplicate and the new item
            total_price += price - duplicate_prices.pop()

            # Recalculate the elegance and update max_elegance if it's greater
            max_elegance = max(max_elegance, total_price + len(seen_colors) ** 2)

        # Return the maximum elegance found
        return max_elegance

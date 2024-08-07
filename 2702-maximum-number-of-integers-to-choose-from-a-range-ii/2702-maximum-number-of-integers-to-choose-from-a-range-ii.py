class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2557.Maximum%20Number%20of%20Integers%20to%20Choose%20From%20a%20Range%20II
        
        # Extend the banned list to include 0 and n+1 to simplify range calculations
        banned.extend([0, n + 1])
        # Ensure the banned list is unique and sorted
        banned = sorted(set(banned))      
        # Initialize the answer to 0
        answer = 0
      
        # Loop through each pair of consecutive banned numbers (Using pairwise requires itertools in Python 3.8+)
        for i, j in zip(banned, banned[1:]):
            # We use binary search to find the maximum count of numbers
            # between a pair of banned numbers that we can sum without exceeding maxSum
            left, right = 0, j - i - 1
          
            while left < right:
                # Calculate the midpoint for binary search
                mid = (left + right + 1) // 2
              
                # Calculate the sum of an arithmetic series from lower_bound+1 to lower_bound+mid
                if ((i + 1 + i + mid) * mid) // 2 <= maxSum:
                    # If the sum is less than or equal to maxSum, move the left bound up
                    left = mid
                else:
                    # Otherwise, move the right bound down
                    right = mid - 1
          
            # Add the count of numbers found to the answer
            answer += left
            # Decrease maxSum by the sum of numbers we've added to the answer
            maxSum -= ((i + 1 + i + left) * left) // 2
          
            # If maxSum becomes zero or negative, we cannot add any more numbers
            if maxSum <= 0:
                break
      
        # Return the total count of numbers we can sum
        return answer
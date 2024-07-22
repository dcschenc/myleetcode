class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1643.Kth%20Smallest%20Instructions
        vertical, horizontal = destination
        answer = []

        # Loop through the total number of moves (sum of vertical and horizontal moves)
        for _ in range(horizontal + vertical):
            # If there are no more horizontal moves, all remaining moves are vertical
            if horizontal == 0:
                answer.append("V")
            else:
                # Calculate the number of combinations that start with a horizontal move
                combinations_with_h = comb(horizontal + vertical - 1, horizontal - 1)
              
                # If the kth path is greater than the number of paths starting with 'H', 
                # then the path must start with a 'V' move instead.
                if k > combinations_with_h:
                    answer.append("V")
                    vertical -= 1
                    k -= combinations_with_h
                else:
                    # Otherwise, the path starts with a 'H' move
                    answer.append("H")
                    horizontal -= 1
      
        # Join all moves into a single path string and return it
        return "".join(answer)
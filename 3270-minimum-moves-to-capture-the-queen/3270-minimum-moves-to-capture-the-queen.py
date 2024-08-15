class Solution:
    def minMovesToCaptureTheQueen(self, rook_x: int, rook_y: int, bishop_x: int, bishop_y: int, queen_x: int, queen_y: int) -> int:
        # https://algo.monster/liteproblems/3001
        def check(directions, start_x, start_y, blocker_x, blocker_y) -> bool:
            # Iterate over the directions pairwise (e.g., up, right, down, left for a rook)
            for dx, dy in zip(directions, directions[1:]):
                # Try moving the piece in the current direction
                for k in range(1, 8):  # The chessboard is 8x8
                    x = start_x + dx * k
                    y = start_y + dy * k
                    # Check board boundaries and blocker position
                    if not (1 <= x <= 8 and 1 <= y <= 8) or (x, y) == (blocker_x, blocker_y):
                        break
                    # Check if we've reached the queen's position
                    if (x, y) == (queen_x, queen_y):
                        return True
            return False

        # Directions that the rook can move: up, right, down, left
        rook_directions = (-1, 0, 1, 0, -1)
        # Directions that the bishop can move: up-right, down-right, down-left, up-left
        bishop_directions = (-1, 1, 1, -1, -1)
      
        # Check if the rook can capture the queen considering the bishop as a blocker, or
        # if the bishop can capture the queen considering the rook as a blocker
        # If either can capture in one move, return 1; otherwise, it will take at least 2 moves
        return 1 if check(rook_directions, rook_x, rook_y, bishop_x, bishop_y) or check(bishop_directions, bishop_x, bishop_y, rook_x, rook_y) else 2

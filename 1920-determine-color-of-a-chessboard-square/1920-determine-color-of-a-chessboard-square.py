class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        c, r = coordinates
        if c in 'aceg':
            if r in '1357':
                return False
            return True
        else:
            if r in '2468':
                return False
            return True
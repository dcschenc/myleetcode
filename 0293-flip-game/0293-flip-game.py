class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        n = len(currentState)
        result = []
        i = 1
        while i < n:
            if currentState[i-1:i+1] == '++':
                result.append(currentState[:i-1] + '--' + currentState[i+1:]) 
            i += 1
        return result
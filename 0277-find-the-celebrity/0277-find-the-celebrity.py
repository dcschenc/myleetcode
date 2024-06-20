# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # First pass: Find a potential celebrity candidate
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i

        # Second pass: Verify if the candidate is a celebrity
        for i in range(n):
            if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
                return -1

        return candidate
        # celebrity = [True] * n
        # for i in range(n):
        #     for j in range(i, n):
        #         if knows(i, j):
        #             celebrity[i] = False
        #         if knows[j, i]:
        #             celebrity[j] = False
        
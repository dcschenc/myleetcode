class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        n = len(s1)
        if all(s1[i] <= s2[i] for i in range(n)) or all(s2[i] <= s1[i] for i in range(n)):
            return True
        return False

        # ans = True
        # for i in range(n):
        #     if s1[i] > s2[i]:
        #         ans = False
        #         break
        # if ans:
        #     return True
        # ans = True
        # for i in range(n):
        #     if s2[i] > s1[i]:
        #         ans = False
        #         break
        # return ans
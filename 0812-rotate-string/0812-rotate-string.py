class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        # idx = s.find(goal[0])
        for i, c in enumerate(s):
            # if idx != -1:
            #     return s[idx:] + s[0:idx] == goal
            if c == goal[0]:
                if s[i:] + s[0:i] == goal:
                    return True

        return False
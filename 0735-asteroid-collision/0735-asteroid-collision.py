class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)
        for i, v in enumerate(asteroids):
            if v > 0:
                stack.append(v)
                continue
            else:
                right_pop = False
                while stack and stack[-1] > 0:
                    if abs(v) > stack[-1]:
                        stack.pop()
                        continue
                    if abs(v) == stack[-1]:
                        stack.pop()
                    right_pop = True
                    break

                if right_pop is False:
                    # if not stack or stack and stack[-1] < 0:
                    stack.append(v)
        return stack
                        
        
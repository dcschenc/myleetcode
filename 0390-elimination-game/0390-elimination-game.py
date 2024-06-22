from collections import deque
class Solution:
    def lastRemaining(self, n: int) -> int:
        left_to_right = True
        remaining = n
        step = 1
        head = 1

        while remaining > 1:
            if left_to_right or remaining % 2 == 1:
                head += step

            remaining //= 2
            step *= 2
            left_to_right = not left_to_right

        return head

        # Memory Limit Exceeded
        # queue = deque()
        # for i in range(1, n+1):
        #     queue.append(i)
        # while len(queue) > 1:
        #     for i in range(len(queue)):                
        #         if i%2 == 1:
        #             queue.append(queue.popleft())
        #         else:
        #             queue.popleft()
        #     queue.reverse()
        # return queue.popleft()

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1823.Find%20the%20Winner%20of%20the%20Circular%20Game
        # The winner index in zero-based index
        winner = 0  # Base case: when there's only one player left
        for i in range(2, n + 1):
            winner = (winner + k) % i
        
        # Convert from zero-based index to one-based index
        return winner + 1

        queue = deque()
        for i in range(1, n+1):
            queue.append(i)
        cur = 0
        while len(queue) > 1:
            idx = (cur + k - 1) % len(queue)
            # print(queue, idx)
            del queue[idx]
            cur = (idx) % len(queue)
        return queue[0]
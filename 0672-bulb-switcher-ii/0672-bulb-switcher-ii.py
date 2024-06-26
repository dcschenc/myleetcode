class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        ops = (0b111111, 0b010101, 0b101010, 0b100100)
        n = min(n, 6)
        vis = set()
        for mask in range(1 << 4):
            cnt = mask.bit_count()
            if cnt <= presses and cnt % 2 == presses % 2:
                t = 0
                for i, op in enumerate(ops):
                    if (mask >> i) & 1:
                        t ^= op
                t &= (1 << 6) - 1
                t >>= 6 - n
                vis.add(t)
        return len(vis)
        
        bulbs = tuple([1] * n)
        queue, visited = deque(), set()
        queue.append((bulbs))
        ans = set()
        press = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()                                
                if (cur, press) in visited:
                    continue
                visited.add((cur, press))
                if press == presses:
                    ans.add(cur)
                    continue
                cur_1 = [0 if v == 1 else 1 for v in cur]
                queue.append((tuple(cur_1), press + 1))
                cur_2 = list(cur)
                for i in range(1, n, 2):
                    cur_2[i] = 1 if cur_2[i] == 0 else 0
                queue.append((tuple(cur_2), press + 1))

                cur_3 = list(cur)
                # print(cur_3)
                for i in range(0, n, 2):
                    cur_3[i] = 1 if cur_3[i] == 0 else 0               
                queue.append((tuple(cur_3), press + 1))

                cur_4 = list(cur)
                j, k = 0, 1
                while j < n:
                    cur_4[j] = 1 if cur_4[j] == 0 else 0
                    j = 3 * k + 1
                    k + 1
                cur_4 = tuple(cur_4)
                queue.append((cur_4, press + 1))
            # print(queue)

        return len(ans)

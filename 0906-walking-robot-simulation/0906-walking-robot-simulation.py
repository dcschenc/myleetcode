class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ob = set()
        for ox, oy in obstacles:
            ob.add((ox, oy))
        ans = 0
        x, y = 0, 0        
        faces = 'NESW'
        dr = {'N': (0, 1), 'E':(1, 0), 'S': (0, -1), 'W': (-1, 0)}
        cur_face = 'N'
        for c in commands:
            cur_idx = faces.index(cur_face)
            if c == -2:
                nxt_idx = (cur_idx - 1) % 4
                cur_face = faces[nxt_idx]
            elif c == -1:
                nxt_idx = (cur_idx + 1) % 4
                cur_face = faces[nxt_idx]
            else:            
                # if cur_face == 'N':
                #     dx, dy = 0, c
                # elif cur_face == 'E':
                #     dx, dy = c, 0
                # elif cur_face == 'S':
                #     dx, dy = 0, -c
                # else:
                #     dx, dy = -c, 0
                dx, dy = dr[cur_face]
                for i in range(c):
                    if (x + dx, y + dy) in ob:
                        break
                    x, y = x + dx, y + dy
                ans = max(ans, x ** 2 + y ** 2)
            # print(cur_face, x, y)
        return ans
            

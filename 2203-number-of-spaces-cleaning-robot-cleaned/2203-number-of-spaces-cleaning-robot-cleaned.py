# from sortedcontainers import SortedSet
class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2061.Number%20of%20Spaces%20Cleaning%20Robot%20Cleaned
        m, n = len(room), len(room[0])
        seen, ans = set(), set([(0, 0)])
        x, y = 0, 0
        dx, dy = 0, 1        
        while True:        
            if (x, y, dx, dy) in seen:
                break
            seen.add((x, y, dx, dy))     
            new_x, new_y = x + dx, y + dy       
            if 0 <= new_x <= m-1 and 0 <= new_y <= n-1 and room[new_x][new_y] == 0:
                ans.add((new_x, new_y))
                x, y = new_x, new_y         
            else:
                if dx == 0 and dy == 1:
                    dx, dy = 1, 0
                elif dx == 1 and dy == 0:
                    dx, dy = 0, -1
                elif dx == 0 and dy == -1:
                    dx, dy = -1, 0
                elif dx == -1 and dy == 0:
                    dx, dy = 0, 1
        return len(ans)
            


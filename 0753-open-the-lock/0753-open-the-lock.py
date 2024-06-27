from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        seen = set('0000')
        q = deque(['0000'])
        levels = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return levels
                for i in range(4):
                    num = int(cur[i])
                    up = cur[:i] + str((num + 1) % 10) + cur[i+1:]
                    if up not in seen and up not in deadends:
                        q.append(up)
                        seen.add(up)
                    down = cur[:i] + str((num - 1) % 10) + cur[i+1:]
                    if down not in seen and down not in deadends:
                        q.append(down)
                        seen.add(down)
            levels += 1
        return -1 
        
#         start = '0000'
#         visited = dict()
#         queue = deque()
#         queue.append(start)
#         visited[start] = 0
#         if '0000' in deadends:
#             return -1
        
#         while queue:
#             curr = queue.popleft()
#             if curr == target:
#                 return visited[curr]
#             level = visited[curr] + 1
#             # print(queue)
#             for i in range(4):
#                 self.get_move(i, True, curr, visited, queue, deadends, level)
#                 self.get_move(i, False, curr, visited, queue, deadends, level)
            
            
#         return -1
                
                
#     def get_move(self, idx, incr, curr, visited, queue, deadends, level):
#         new = curr
#         if incr:
#             char = str((int(new[idx]) + 1)%10)
#         else:
#             tmp = int(new[idx]) - 1
#             if tmp == -1:
#                 char = '9'
#             else:
#                 char = str(tmp)
#         new = new[:idx] + char + new[idx+1:]
#         if new not in visited and new not in deadends:
#             visited[new] = level
#             queue.append(new) 
        
            
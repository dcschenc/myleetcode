from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d, r = 0, 0
        # senate = list(senate)
        num_d = senate.count('D')
        num_r = len(senate) - num_d
        queue = deque(senate)
        # while len(set(queue)) > 1:
        while r < num_r and d < num_d:
            s = queue.popleft()
            if s == 'D':
                if d == 0:
                    r += 1
                    queue.append('D')
                else:
                    d -=1
            if s == 'R':
                if r == 0:
                    d += 1
                    queue.append('R')
                else:
                    r -=1
        if queue.pop() == 'R':
            return 'Radiant'
        return 'Dire'

        # print(r,d)
        # if d == 0 and r==0:
        #     if senate[0] == 'D':
        #         r += 1
        #     else:
        #         d +=1
        if d > 0:
            return 'Radiant'
        return 'Dire'


        # queue = list(senate)
        # queue.reverse()
        # # print(queue)
        # while len(queue) > 0:
        #     val = queue.pop()
        #     queue.insert(0,val)
        #     if val != queue[-1]:
        #         queue.pop()
        #     # if queue[-1] != queue[0]:
        #     #     queue.pop(0)
        #     # if queue[-1] == 'R':
        #     #     try:                    
        #     #         queue.remove('D')
        #     #     except:
        #     #         pass
        #     # else:
        #     #     try:                    
        #     #         queue.remove('R')
        #     #     except:
        #     #         pass
        #     # queue.insert(0, queue[-1])
        #     # queue.pop()
        #     # print(queue, len(set(queue)), len(queue))
        #     if len(set(queue)) ==  1:
        #         if queue[0] == 'R':
        #             return 'Radiant'
        #         else:
        #             return 'Dire'

        # while queue:
            # print(queue.pop())
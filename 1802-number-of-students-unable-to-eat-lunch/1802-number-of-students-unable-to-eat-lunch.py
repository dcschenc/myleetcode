from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1700.Number%20of%20Students%20Unable%20to%20Eat%20Lunch
        cnt = Counter(students)
        for v in sandwiches:
            if cnt[v] == 0:
                return cnt[v ^ 1]
            cnt[v] -= 1
        return 0
        
        queue = deque(students)
        cont = True
        while queue and cont and len(sandwiches) > 0:
            cont = False
            for i in range(len(queue)):
                student = queue.popleft()
                if student != sandwiches[0]:
                    queue.append(student)
                else:
                    sandwiches = sandwiches[1:]
                    cont = True
        return len(queue)

      
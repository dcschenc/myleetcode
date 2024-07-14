from collections import deque
class Solution:
    # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1361.Validate%20Binary%20Tree%20Nodes
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def find_root():
            children = set(leftChild) | set(rightChild)
            for i in range(n):
                if i not in children:
                    return i
            return -1
        
        root = find_root()
        if root == -1:
            return False

        queue = deque()
        queue.append(root)
        visited = set()
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node in visited:
                    return False
                visited.add(node)
                if leftChild[node] != -1:                    
                    queue.append(leftChild[node])
                if rightChild[node] != -1:
                    queue.append(rightChild[node])

        return True if len(visited) == n else False
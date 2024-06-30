# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # https://leetcode.com/problems/binary-tree-cameras/editorial/
        self.ans = 0
        covered = {None}

        def dfs(node, par = None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if (par is None and node not in covered or
                        node.left not in covered or node.right not in covered):
                    self.ans += 1
                    covered.update({node, par, node.left, node.right})

        dfs(root)
        return self.ans


        # https://github.com/doocs/leetcode/tree/main/solution/0900-0999/0968.Binary%20Tree%20Cameras
        # a：当前节点有摄像头
        # b：当前节点无摄像头，但被子节点监控
        # c：当前节点无摄像头，也没被子节点监控
        def dfs(node):
            if node is None:
                return inf, 0, 0
            la, lb, lc = dfs(node.left)
            ra, rb, rc = dfs(node.right)
            a = min(la, lb, lc) + min(ra, rb, rc) + 1
            b = min(la + rb, lb + ra, la + ra)
            c = lb + rb
            return a, b, c

        a, b, _ = dfs(root)
        return min(a, b)
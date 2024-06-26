"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(emp):
            ans = emp.importance
            for nxt in emp.subordinates:
                ans += dfs(hm[nxt])
            return ans
        
        hm = {}
        for emp in employees:
            hm[emp.id] = emp

        return dfs(hm[id])

        
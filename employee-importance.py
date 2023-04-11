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

        total = 0
        mapping = defaultdict(int)
        for employee in employees:
            mapping[employee.id] = employee

        def dfs(employee):
            nonlocal total
            total += employee.importance

            for e in employee.subordinates:
                dfs(mapping[e])


        for employee in employees:
            if employee.id == id:
                dfs(employee)
                break

        return total
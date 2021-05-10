#
# @lc app=leetcode.cn id=690 lang=python3
#
# [690] 员工的重要性
#

# @lc code=start
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
        emp_list = {employee.id: employee for employee in employees}

        def dfs(idx):
            employee = emp_list[idx]
            total = employee.importance + sum(dfs(sub_idx) for sub_idx in employee.subordinates)
            return total

        return dfs(id)
# @lc code=end


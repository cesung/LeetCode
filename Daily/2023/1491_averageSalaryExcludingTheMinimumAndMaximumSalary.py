from typing import *

class Solution:
    def average(self, salary: List[int]) -> float:
        size = len(salary)
        max_salary, min_salary = max(salary), min(salary)
        ttl_salary = sum(salary)
        ttl_salary -= (max_salary + min_salary)

        return ttl_salary / (size - 2)
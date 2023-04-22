from typing import *

class Solution:
    def profitableSchemes(self, n: int, min_profit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        project_size = len(group)
        group = [0] + group
        profit = [0] + profit

        # dp[project][num_ppl][profit], 1-index
        dp = [[[0 for _ in range(min_profit + 1)] for _ in range(n + 1)] for _ in range(project_size + 1)]
        dp[0][0][0] = 1

        for project_idx in range(project_size): # to project_size - 1, includsive
            for num_ppl in range(n + 1):
                for num_profit in range(min_profit + 1):
                    # do not take project_idx
                    dp[project_idx + 1][num_ppl][num_profit] += dp[project_idx][num_ppl][num_profit]
                    dp[project_idx + 1][num_ppl][num_profit] %= MOD

                    # take project_idx
                    if num_ppl + group[project_idx + 1] <= n:
                        dp[project_idx + 1][num_ppl + group[project_idx + 1]][min(min_profit, num_profit + profit[project_idx + 1])] += (
                            dp[project_idx][num_ppl][num_profit]
                        )
                        dp[project_idx + 1][num_ppl + group[project_idx + 1]][min(min_profit, num_profit + profit[project_idx + 1])] %= MOD
            
        ret = 0
        for num_ppl in range(n + 1):
            ret += dp[project_size][num_ppl][min_profit]
            ret %= MOD
        
        return ret
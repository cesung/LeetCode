from typing import *
from collections import defaultdict

class Solution:
    def dfs(self, left, right):
        # boundary condition when left == right, take it and return
        if left == right:
            return self.nums[left]
    
        if (left, right) in self.dp:
            return self.dp[(left, right)]
    
        # take left
        self.dp[ (left, right) ] = max( 
            self.dp[ (left, right) ],
            # reward of taking left
            self.nums[left] +
            # all - best can obtain by opponent 
            # sum( (left, right] ) - dp[left + 1, right]
            ((self.prefix_sum[right] - self.prefix_sum[left] ) - self.dfs(left + 1, right))
            
        )
        
        # take right
        self.dp[ (left, right) ] = max(
            self.dp[ (left, right)],
            # reward of taking right
            self.nums[right] + 
            # all - best can obtain by opponent
            # sum( [left, right) ) - dp[left, right - 1]
            (self.prefix_sum[right - 1] - (self.prefix_sum[left - 1] if left - 1 != -1 else 0)) - self.dfs(left, right - 1)
        )
        
        return self.dp[ (left, right) ]
    
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # prefix_sum array, O(n)
        self.prefix_sum = [nums[0]]
        for idx in range(1, n):
            self.prefix_sum.append(self.prefix_sum[-1] + nums[idx])
        self.nums = nums
        
        # dp[(left, right)]: the maximum score that can obtain by choosing numbers within range [left, right]
        self.dp = defaultdict(int)
        
        player1 = self.dfs(0, n - 1)
        # player2 = all - player1
        player2 = self.prefix_sum[-1] - player1
        
        return player1 >= player2
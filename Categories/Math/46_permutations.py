from typing import *

class Solution:
    def dfs(self, cnt: int, permut: List[int]) -> None:
        if cnt == self.n:
            self.permuts.append(permut[:])
            return

        for idx in range(self.n):
            if self.vis[idx] == True:
                continue

            self.vis[idx] = True
            self.dfs(cnt + 1, permut + [self.nums[idx]])
            self.vis[idx] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        self.nums = nums
        self.vis = [False for _ in range(self.n)]
        self.permuts = []

        self.dfs(0, [])

        return self.permuts
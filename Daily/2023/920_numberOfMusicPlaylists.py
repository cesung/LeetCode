from typing import *
from collections import defaultdict

class Solution:
    def dfs(self, num_remaining: int, num_unique_played: int) -> int:
        # num_remaining: number of songs that can still play before reaching the base case (num_remaining == 0)
        # num_unique_played => number of unique songs that has already played
        if num_remaining == 0 and num_unique_played == self.n:
            return 1
        if num_remaining == 0 or num_unique_played > self.n:
            return 0
        
        if (num_remaining, num_unique_played) in self.dp:
            return self.dp[ (num_remaining, num_unique_played) ]

        # play a new songs
        self.dp[ (num_remaining, num_unique_played) ] += (self.n - num_unique_played) * self.dfs(num_remaining - 1, num_unique_played + 1)

        if num_unique_played > self.k:
            # play an old song
            self.dp[ (num_remaining, num_unique_played) ] += (num_unique_played - self.k) * self.dfs(num_remaining - 1, num_unique_played)

        self.dp[ (num_remaining, num_unique_played) ] %= self.MOD
        

        return self.dp[ (num_remaining, num_unique_played) ]


    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        self.MOD = 10**9 + 7
        self.n = n
        self.k = k

        self.dp = defaultdict(int)
        
        return self.dfs(goal, 0)
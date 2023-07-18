class Solution:
    def dfs(self, idx):
        if idx == self.size:
            return True

        if self.rcd[idx] != -1:
            return self.dfs(idx + 1)

        for num in range(self.n, 0, -1):
            if self.num_vis[num] == True:
                continue

            if (
                num > 1 and 
                (
                    idx + num >= self.size or
                    self.rcd[idx + num] != -1
                )
            ):
                continue
            
            self.num_vis[num] = True
            self.rcd[idx] = num
            if num > 1:
                self.rcd[idx + num] = num
            

            if not self.dfs(idx + 1):
                self.num_vis[num] = False
                self.rcd[idx] = -1
                if num > 1:
                    self.rcd[idx + num] = -1
            else:
                return True
        
        return False


    def constructDistancedSequence(self, n: int) -> List[int]:
        self.n = n
        self.size = 2*n - 1
        self.rcd = [-1 for _ in range(self.size)]
        self.num_vis = [False for _ in range(self.n + 1)]
        self.dfs(0)

        return self.rcd
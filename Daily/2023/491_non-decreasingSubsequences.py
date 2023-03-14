class Solution:

    def dfs(self, idx, seq):
        if idx == self.size:
            if len(seq) >= 2:
                self.seqs.add(" ".join(map(str, seq[:])))
            return
        
        if not seq or self.nums[idx] >= seq[-1]:
            self.dfs(idx + 1, seq + [self.nums[idx]])
            self.dfs(idx + 1, seq)
        else:
            self.dfs(idx + 1, seq)

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.size = len(nums)
        self.nums = nums
        self.seqs = set()
        self.dfs(0, [])
        
        return [list(map(int, seq.split())) for seq in self.seqs]

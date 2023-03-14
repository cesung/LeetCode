class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        num_votes = [0 for _ in range(n + 1)]
        vis = set()
        for ai, bi in trust:
            vis.add(ai)
            num_votes[bi] += 1

        for idx in range(1, n + 1):
            if num_votes[idx] == n - 1 and idx not in vis:
                return idx
        
        return -1

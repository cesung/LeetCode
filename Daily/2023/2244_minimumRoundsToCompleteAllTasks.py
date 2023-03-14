from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cntr = Counter(tasks)
        rounds = 0

        for _, freq in cntr.items():
            if freq == 1:
                return -1
            
            rounds += freq // 3 if freq % 3 == 0 else  freq // 3 + 1
        
        return rounds

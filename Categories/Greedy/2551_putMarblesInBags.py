class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        size = len(weights)
        
        scores = []
        for idx in range(1, size):
            scores.append(weights[idx] + weights[idx - 1])
        
        scores_size = len(scores)
        scores.sort()
        
        min_score = max_score = weights[0] + weights[-1]
        for idx in range(k - 1):
            min_score += scores[idx]
        
        for idx in range(k - 1):
            max_score += scores[scores_size - 1 - idx]
        
        return max_score - min_score

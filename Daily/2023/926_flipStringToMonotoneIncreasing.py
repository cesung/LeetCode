class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        INF = float('inf')
        size = len(s)
        ttl = sum(map(int, s))
        
        one_to_left = [0]
        for idx in range(size):
            one_to_left.append(
                one_to_left[-1] + 1
                if s[idx] == '1'
                else one_to_left[-1]
            )

        zero_to_right = [0]
        for idx in range(size - 1, -1, -1):
            zero_to_right.append(
                zero_to_right[-1] + 1
                if s[idx] == '0'
                else zero_to_right[-1]
            )
        zero_to_right = zero_to_right[::-1]
    
        min_flip = INF
        for idx in range(size + 1):
            min_flip = min(
                min_flip,
                one_to_left[idx] + zero_to_right[idx],
            )
        
        return min_flip

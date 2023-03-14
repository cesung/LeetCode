class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        size = len(gas)
        remaining = [gas[idx] - cost[idx] for idx in range(size)]
        ttl = sum(remaining)

        if ttl < 0:
            return -1
        
        ret = 0
        cur = 0
        for idx in range(size):
            cur += remaining[idx]

            if cur < 0:
                ret = idx + 1
                cur = 0
            
        return ret

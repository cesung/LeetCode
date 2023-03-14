class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        size = len(arr)
        ttl = sum(arr)
        if ttl % 3 != 0:
            return False

        cnt, cur = 0, 0
        for idx in range(size):
            cur += arr[idx]
            if cur == ttl // 3:
                cur = 0
                cnt += 1
            if cnt == 3:
                return True
        
        return False

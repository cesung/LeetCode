class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        cnt, maxv = 0, -1

        for num in arr:
            cnt += 1
            maxv = max(
                maxv, 
                num
            )

            if maxv + 1 == cnt:
                chunks += 1
    
        return chunks

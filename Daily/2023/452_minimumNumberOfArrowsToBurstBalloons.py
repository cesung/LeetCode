class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        size = len(points)
        cnt = 1
        right = points[0][1]
        for idx in range(1, size):
            if points[idx][0] > right:
                right = points[idx][1]
                cnt += 1
        
        return cnt

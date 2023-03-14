from collections import defaultdict

class Solution:

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def maxPoints(self, points: List[List[int]]) -> int:

        INT_MAX = float('inf')

        size = len(points)
        if size <= 1:
            return size

        max_num_points = 1
        for idx in range(size):

            slope = defaultdict(int)
            for jdx in range(size):
                if idx == jdx:
                    continue
                dx = points[idx][0] - points[jdx][0]
                dy = points[idx][1] - points[jdx][1]

                xy_gcd = self.gcd(dx, dy)
                dx //= xy_gcd
                dy //= xy_gcd

                if dx == 0:
                    slope[ (INT_MAX, INT_MAX) ] += 1
                    continue
                
                slope[ (dy, dx) ] += 1

            max_num_points = max(max_num_points, max(slope.values()))
        
        return max_num_points + 1
            

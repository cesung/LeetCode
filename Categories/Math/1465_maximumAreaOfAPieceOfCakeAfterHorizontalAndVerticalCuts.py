class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10**9 + 7
        horizontalCuts.sort()
        verticalCuts.sort()

        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]

        max_horizontal_diff = -1
        for idx in range(1, len(horizontalCuts)):
            max_horizontal_diff = max(max_horizontal_diff, horizontalCuts[idx] - horizontalCuts[idx - 1])
        max_vertical_diff = -1
        for idx in range(1, len(verticalCuts)):
            max_vertical_diff = max(max_vertical_diff, verticalCuts[idx] - verticalCuts[idx - 1])

        return (max_horizontal_diff * max_vertical_diff) % MOD

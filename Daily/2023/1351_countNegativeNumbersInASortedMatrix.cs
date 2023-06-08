public class Solution {
    public int CountNegatives(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        int jdx = n - 1, cnt = 0;
        for (int idx = 0; idx < m; idx++) {
            while (
                jdx >= 0 &&
                grid[idx][jdx] < 0
            ) {
                cnt += (m - idx);
                jdx -= 1;
            }
        }

        return cnt;
    }
}
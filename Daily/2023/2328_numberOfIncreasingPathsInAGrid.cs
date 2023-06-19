public class Solution {
    int MOD = (int)Math.Pow(10.0, 9.0) + 7;
    int num_rows, num_cols;
    int [,] dp;
    int [,] directions;

    private int dfs(ref int[][] grid, int row, int col) {
        if (dp[row, col] != 0) {
            return dp[row, col];
        }

        dp[row, col] = 1;
        int nrow, ncol;
        for (int dir = 0; dir < 4; dir++) {
            nrow = row + directions[dir, 0];
            ncol = col + directions[dir, 1];

            if (
                nrow < 0 ||
                nrow >= num_rows ||
                ncol < 0 ||
                ncol >= num_cols
            ) {
                continue;
            }

            if (grid[nrow][ncol] >= grid[row][col]) {
                continue;
            }

            dp[row, col] = (dp[row, col] + dfs(ref grid, nrow, ncol)) % MOD;
        } 
    
        return dp[row, col];
    }

    public int CountPaths(int[][] grid) {
        // graph[row][col]: strickly increasing path end at position (row, col)
        num_rows = grid.Length;
        num_cols = grid[0].Length;

        dp = new int [num_rows, num_cols];
        directions = new int [4, 2] {
            {+1, 0},
            {0, +1},
            {-1, 0},
            {0, -1}
        };

        int ret = 0;
        for (int row = 0; row < num_rows; row++) {
            for (int col = 0; col < num_cols; col++) {
                ret = (ret + dfs(ref grid, row, col) ) % MOD;
            }
        }

        return ret;
    }
}
public class Solution {
    int num_rows, num_cols;
    int[][] dp;
    int[][] directions;

    private int dfs(ref int[][] matrix, int row, int col) {
        if (dp[row][col] != 0) {
            return dp[row][col];
        }

        dp[row][col] = 1;
        int nrow, ncol, drow, dcol;
        foreach(int[] direction in directions) {
            drow = direction[0];
            dcol = direction[1];
            nrow = row + drow;
            ncol = col + dcol;

            if (
                nrow < 0 ||
                nrow >= num_rows ||
                ncol < 0 ||
                ncol >= num_cols
            ) {
                continue;
            }

            if ( matrix[nrow][ncol] >= matrix[row][col] ) {
                continue;
            }
            
            dp[row][col] = Math.Max(
                dp[row][col],
                dfs(ref matrix, nrow, ncol) + 1
            );
        }

        return dp[row][col];
    }

    public int LongestIncreasingPath(int[][] matrix) {
        num_rows = matrix.Length;
        num_cols = matrix[0].Length;

        // dp[row][col]: longest increasing path ending at position (row, col)
        dp = new int[num_rows][];
        for (int row = 0; row < num_rows; row++) {
            dp[row] = new int[num_cols];
        }

        directions = new int [][] 
        {
            new int[] {+1, 0},
            new int[] {0, +1},
            new int[] {-1, 0},
            new int[] {0, -1}
        };

        int ret = 0;
        for (int row = 0; row < num_rows; row++) {
            for (int col = 0; col < num_cols; col++) {
                ret = Math.Max(
                    ret,
                    dfs(ref matrix, row, col)
                );
            }
        }

        return ret;
    }
}
public class Solution {
    public int NumSubmat(int[][] mat) {
        int num_rows = mat.Length, num_cols = mat[0].Length;
        int[][] dp = new int[num_rows][];
        for (int row = 0; row < num_rows; row++) {
            dp[row] = new int[num_cols];
        }

        int cnt;
        for (int row = 0; row < num_rows; row++) {
            cnt = 0;
            for (int col = 0; col < num_cols; col++) {
                cnt = mat[row][col] == 1 ? cnt + 1 : 0;
                dp[row][col] = cnt;
            }
        }

        int ret = 0;
        for (int row = 0; row < num_rows; row++) {
            for (int col = 0; col < num_cols; col++) {
                cnt = Int32.MaxValue;
                for (int _row = row; _row < num_rows; _row++) {
                    cnt = Math.Min(
                        cnt,
                        dp[_row][col]
                    );
                    ret += cnt;
                }
            }
        }

        return ret;
    }
}
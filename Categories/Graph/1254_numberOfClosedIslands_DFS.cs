public class Solution {
    int m, n;
    HashSet<Tuple<int, int>> vis = new HashSet<Tuple<int, int>>();
    List<List<int>> directions = new List<List<int>> {
        new List<int> {+1, 0},
        new List<int> {0, +1},
        new List<int> {-1, 0},
        new List<int> {0, -1},
    };

    private bool dfs(int row, int col, int[][] grid) {
        if (
            row < 0 || row == m ||
            col < 0 || col == n
        ) {
            return false;
        }

        if (
            grid[row][col] == 1 ||
            vis.Contains( Tuple.Create(row, col) )
        ) {
            return true;
        } 
        vis.Add( Tuple.Create(row, col) );

        int nrow, ncol;
        bool suc = true;
        foreach (var direction in directions) {
            nrow = row + direction[0];
            ncol = col + direction[1];
            suc &= dfs(nrow, ncol, grid);
        }

        return suc;
    }

    public int ClosedIsland(int[][] grid) {
        m = grid.Length;
        n = grid[0].Length;
        int cnt = 0;

        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (
                    grid[row][col] == 0 &&
                    !vis.Contains( Tuple.Create(row, col))
                ) {
                    cnt += dfs(row, col, grid) == true ? 1 : 0;
                }
            }
        }
        return cnt;
    }
}
public class Solution {
    public int EqualPairs(int[][] grid) {
        int numRows = grid.Length, numCols = grid[0].Length;
        Dictionary<string, int> rowEmbeddingCounter = new Dictionary<string, int>();

        for (int rowIdx = 0; rowIdx < numRows; rowIdx+= 1) {
            string rowEmbedding = String.Join(",", grid[rowIdx]);
            if (!rowEmbeddingCounter.ContainsKey(rowEmbedding)) {
                rowEmbeddingCounter.Add(rowEmbedding, 1);
            }
            else {
                rowEmbeddingCounter[rowEmbedding] += 1;
            }
        }

        int cnt = 0;
        List<int> col = new List<int>();
        for (int colIdx = 0; colIdx < numCols; colIdx += 1) {
            col.Clear();
            for (int rowIdx = 0; rowIdx < numRows; rowIdx += 1) {
                col.Add(grid[rowIdx][colIdx]);
            }
            string colEmbedding = String.Join(",", col);
            cnt += rowEmbeddingCounter.ContainsKey(colEmbedding) ? rowEmbeddingCounter[colEmbedding] : 0;
        }

        return cnt;
    }
}
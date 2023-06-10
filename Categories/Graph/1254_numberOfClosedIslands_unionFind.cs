public class UnionFind {
    public int[] parents;
    public int[] ranks;

    public UnionFind(int size) {
        parents = new int[size];
        for (int idx = 0; idx < size; idx++) {
            parents[idx] = idx;
        }
        ranks = new int[size];
        for (int idx = 0; idx < size; idx++) {
            ranks[idx] = 1;
        }
    }

    public int Find(int node) {
        int root = node;
        while (root != parents[root]) {
            root = parents[root];
        }

        int cur = node, nxt;
        while (cur != root) {
            nxt = parents[cur];
            parents[cur] = root;
            cur = nxt;
        }

        return root;
    }

    public void Union(int node1, int node2) {
        int parent1 = Find(node1);
        int parent2 = Find(node2);

        if (parent1 == parent2) {
            return;
        }

        if (ranks[parent1] > ranks[parent2]) {
            parents[parent1] = parent2;
            ranks[parent1] += ranks[parent2];
        }
        else {
            parents[parent2] = parent1;
            ranks[parent2] += ranks[parent1];
        }
    }
}

public class Solution {
    public List<List<int>> directions = new List<List<int>>{
        new List<int> {+1, 0},
        new List<int> {0, +1},
        new List<int> {-1, 0},
        new List<int> {0, -1},
    };
    // m * n matrix
    int m, n;

    public int ClosedIsland(int[][] grid) {
        m = grid.Length; n = grid[0].Length;
        var unionFind = new UnionFind(m * n);

        int newRow, newCol;
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (grid[row][col] == 1) {
                    continue;
                }
                foreach (var direction in directions) {
                    newRow = row + direction[0];
                    newCol = col + direction[1];

                    if (
                        newRow < 0 || newRow == m ||
                        newCol < 0 || newCol == n
                    ) {
                        continue;
                    }

                    if (grid[newRow][newCol] == 0) {
                        unionFind.Union(
                            row * n + col,
                            newRow * n + newCol
                        );
                    }
                }
            }
        }

        int parent;
        var islands = new HashSet<int>();
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (grid[row][col] == 1) {
                    continue;
                }
                islands.Add(unionFind.Find(row * n + col));
            }
        }

        for (int row = 0; row < m; row++) {
            if (grid[row][0] == 0) {
                parent = unionFind.Find(row * n);
                if (islands.Contains(parent)) {
                    islands.Remove(parent);
                }
            }
            if (grid[row][n - 1] == 0) {
                parent = unionFind.Find(row * n + n - 1);
                if (islands.Contains(parent)) {
                    islands.Remove(parent);
                }
            }
        }

        for (int col = 0; col < n; col++) {
            if (grid[0][col] == 0) {
                parent = unionFind.Find(col);
                if (islands.Contains(parent)) {
                    islands.Remove(parent);
                }
            }
            if (grid[m - 1][col] == 0) {
                parent = unionFind.Find( (m - 1) * n + col);
                if (islands.Contains(parent)) {
                    islands.Remove(parent);
                }
            }
        }
        return islands.Count();
    }
}
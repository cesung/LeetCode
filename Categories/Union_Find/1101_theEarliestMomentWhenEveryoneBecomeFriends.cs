public class UnionFind {
    int[] parents;
    int[] ranks;

    public UnionFind(int n) {
        parents = new int[n];
        for (int idx = 0; idx < n; idx++) {
            parents[idx] = idx;
        }
        
        ranks = new int[n];
        for (int idx = 0; idx < n; idx++) {
            ranks[idx] = 1;
        }
    }

    public int find(int n) {
        int root = n;
        while (root != parents[root]) {
            root = parents[root];
        }
        
        int cur = n;
        int nxt;
        while (cur != root) {
            nxt = parents[cur];
            parents[cur] = root;
            cur = nxt;
        }

        return root;
    }

    public bool union(int n1, int n2) {
        int p1 = find(n1), p2 = find(n2);
        if (p1 == p2) {
            return false; 
        }

        if (ranks[p1] > ranks[p2]) {
            ranks[p2] += ranks[p1];
            parents[p1] = p2;
        }
        else {
            ranks[p1] += ranks[p2];
            parents[p2] = p1;
        }

        return true;
    }
}

public class Solution {
    public int EarliestAcq(int[][] logs, int n) {
        logs = logs.OrderBy(log => log[0]).ToArray();
        UnionFind union_find = new UnionFind(n);

        int t, n1, n2;
        int num_groups = n;
        for (int idx = 0; idx < logs.Length; idx++) {
            t = logs[idx][0];
            n1 = logs[idx][1];
            n2 = logs[idx][2];

            if (union_find.union(n1, n2)) {
                num_groups -= 1;
            }

            if (num_groups == 1) {
                return t;
            }
        }

        return -1;
    }
}
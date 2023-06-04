public class UnionFind
{

    public int[] parents;
    public int[] ranks;

    public UnionFind(int n)
    {
        parents = new int[n + 1];
        for (int idx = 1; idx < n + 1; idx++)
        {
            parents[idx] = idx;
        }
        ranks = new int[n + 1];
        for (int idx = 1; idx < n + 1; idx++)
        {
            ranks[idx] = 1;
        }
    }

    public int Find(int n)
    {
        int root = n;
        while (root != parents[root])
        {
            root = parents[root];
        }

        int nxt = -1;
        int cur = n;
        while (cur != root)
        {
            nxt = parents[cur];
            parents[cur] = root;
            cur = nxt;
        }

        return root;
    }

    public void Union(int n1, int n2)
    {
        int r1 = Find(n1), r2 = Find(n2);
        if (r1 == r2)
        {
            return;
        }
        if (ranks[r1] > ranks[r2])
        {
            parents[r2] = r1;
            ranks[r1] += ranks[r2];
        }
        else
        {
            parents[r1] = r2;
            ranks[r2] += ranks[r1];
        }
    }
}

public class Solution
{
    public int FindCircleNum(int[][] isConnected)
    {
        int n = isConnected.Length;
        var unionFind = new UnionFind(n);

        for (int idx = 1; idx < n + 1; idx++)
        {
            for (int jdx = idx + 1; jdx < n + 1; jdx++)
            {
                if (idx == jdx) continue;
                if (isConnected[idx - 1][jdx - 1] == 1)
                {
                    unionFind.Union(idx, jdx);
                }
            }
        }

        var vis = new HashSet<int>();
        for (int idx = 1; idx < n + 1; idx++)
        {
            vis.Add(unionFind.Find(idx));
        }

        return vis.Count();
    }
}
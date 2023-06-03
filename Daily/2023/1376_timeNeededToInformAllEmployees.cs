public class Solution
{
    private Dictionary<int, List<Tuple<int, int>>> graph = new Dictionary<int, List<Tuple<int, int>>>();
    private int INF = Int32.MaxValue;

    private int dfs(int node)
    {
        int maxTime = -INF;

        if (!graph.ContainsKey(node))
        {
            return 0;
        }

        foreach (var neighbor in graph[node])
        {
            maxTime = Math.Max(
                maxTime,
                neighbor.Item2 + dfs(neighbor.Item1)
            );
        }

        return maxTime == -INF ? 0 : maxTime;
    }

    public int NumOfMinutes(int n, int headID, int[] manager, int[] informTime)
    {
        for (int idx = 0; idx < n; idx++)
        {
            if (!graph.ContainsKey(manager[idx]))
            {
                graph[manager[idx]] = new List<Tuple<int, int>>();
            }
            graph[manager[idx]].Add(Tuple.Create(idx, informTime[idx]));
        }

        return dfs(headID) + informTime[headID];
    }
}
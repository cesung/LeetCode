public class Solution {
    public int MaximalNetworkRank(int n, int[][] roads) {
        Dictionary<int,int> graph = new Dictionary<int,int>();
        HashSet<Tuple<int, int>> vis = new HashSet<Tuple<int, int>>();
        foreach (int[] road in roads) {
            int n1 = road[0], n2 = road[1];
            if (!graph.ContainsKey(n1)) {
                graph.Add(n1, 0);
            }
            graph[n1] += 1;

            if (!graph.ContainsKey(n2)) {
                graph.Add(n2, 0);
            }
            graph[n2] += 1;

            vis.Add(new Tuple<int, int>(n1, n2));
        }

        int max_rank = 0, cur_rank;
        int rank_n1, rank_n2;
        for (int n1 = 0; n1 < n; n1++) {
            for (int n2 = n1 + 1; n2 < n; n2++) {
                rank_n1 = graph.ContainsKey(n1) ? graph[n1] : 0;
                rank_n2 = graph.ContainsKey(n2) ? graph[n2] : 0;
                cur_rank = rank_n1 + rank_n2 + ((
                    vis.Contains(new Tuple<int, int>(n1, n2)) ||
                    vis.Contains(new Tuple<int, int>(n2, n1))
                ) ? -1 : 0);
                max_rank = Math.Max(
                    max_rank,
                    cur_rank
                );
            }
        }

        return max_rank;
    }
}